from django.shortcuts import render
import json
import requests
from bs4 import BeautifulSoup
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from complianceParser import llm_client, stripe_compliance_policy
from django_q.tasks import async_task
from complianceParser.tasks import schedule_compliance_task
from complianceParser.utils import extract_domain
from datetime import datetime

@require_http_methods(["POST"])
def compliance_check(request):
    payload = json.loads(request.body)
    target_website = payload.get("target_website")
    print("queueing up task")
    current_timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    file_path = f"~/talaash/sei/{extract_domain(target_website)}-{current_timestamp}.txt"
    async_task(schedule_compliance_task, target_website, file_path)
    return JsonResponse({"url": target_website, "filepath": file_path})

# TODO: adding validations
# TODO: add exception handling
# TODO: add retries for queue processing
# TODO: add logging

