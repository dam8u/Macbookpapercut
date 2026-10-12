"""Publish the V2 documents to the MOO-100 issue thread, from the same block
sources that produced the .docx and .pdf files."""
import json
import os
import urllib.request

import render

BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/").removesuffix("/api")
KEY = os.environ["PAPERCLIP_API_KEY"]
TASK = os.environ["PAPERCLIP_TASK_ID"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")

HEADER = ("> Also a **.docx** and a **.pdf** in `AgentFilesV2/`. "
          "Where this page and the file differ, the file is the one that was built last.\n")


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(BASE + path, data=data, method=method, headers={
        "Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
        "X-Paperclip-Run-Id": RUN})
    with urllib.request.urlopen(r, timeout=60) as resp:
        body = resp.read().decode()
        return resp.status, (json.loads(body) if body.strip() else None)


def put_doc(key, title, blocks=None, body=None, summary=None):
    md = body if body is not None else HEADER + "\n" + render.to_markdown(blocks)
    payload = {"title": title, "body": md, "format": "markdown"}
    if summary:
        payload["changeSummary"] = summary[:500]
    try:
        cur = req("GET", f"/api/issues/{TASK}/documents/{key}")[1]
        if cur and cur.get("latestRevisionId"):
            payload["baseRevisionId"] = cur["latestRevisionId"]
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    st, _ = req("PUT", f"/api/issues/{TASK}/documents/{key}", payload)
    print(f"{st}  {key}  ({len(md):,} chars)")


def get_doc(key):
    return req("GET", f"/api/issues/{TASK}/documents/{key}")[1]


if __name__ == "__main__":
    import build_annex
    import build_letters
    import build_index
    import amend_fiscal_model

    put_doc("v2-annex-valors-prescore",
            "RESERVE — VaLORS pre-score: the amendment priced before it is offered",
            build_annex.B)
    put_doc("v2-send-packet",
            "SEND INSTRUCTIONS — email text, attachments, hard copy, day-of-send checks",
            build_letters.SP,
            summary="Closing block now complete — name, return address, email and telephone "
                    "applied. Send-from account and display name added to Table 1. Footer note "
                    "rewritten for a personal Gmail. Day-of-send check 3 replaced.")
    put_doc("v2-transmittal",
            "Transmittal — addressees, email channels, signature decision and routing (VRS and DHRM)",
            build_letters.T,
            summary="Closing block recorded as complete in Section 4. Signature recorded as decided (Moody, as author, no organisation). Email "
                    "channel added for each addressee. DHRM address corrected to 600 E Main St, "
                    "17th Floor. FOIA channel ruled out with reasons. Section 4 rewritten.")
    put_doc("v2-data-request",
            "READY TO SEND, NOT YET SENT — data request to VRS and DHRM (13 items, k first)",
            build_letters.DR_SEND,
            summary="The send copy, now complete. Closing block carries name, return address, "
                    "email and telephone; nothing is bracketed. No organisation named. Ready to "
                    "sign and send as-is.")
    put_doc("v2-counsel-question",
            "READY TO SEND, NOT YET SENT — question to VRS counsel on true-up collectability",
            build_letters.CQ_SEND,
            summary="The send copy, now complete. Closing block carries name, return address, "
                    "email and telephone; nothing is bracketed. Ready to sign and send as-is.")
    put_doc("v2-file-index",
            "AgentFilesV2 — V2 file index (all deliverables in .docx / .pdf)",
            build_index.B)
    put_doc("v2-fiscal-model",
            "V2 fiscal model — Retirement Bridge and Retirement Incentive (amendment 1, 12 Oct 2026)",
            amend_fiscal_model.out)
