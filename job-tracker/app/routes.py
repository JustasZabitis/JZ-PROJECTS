from flask import Blueprint, jsonify, request, render_template
from .linkedin_api import get_linkedin_jobs

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/api/linkedin-jobs", methods=["GET"])
def fetch_linkedin_jobs():
    keyword = request.args.get("keyword", "software internship")
    location_id = request.args.get("locationId", "104738515")
    jobs = get_linkedin_jobs(keyword, location_id)
    return jsonify(jobs)
