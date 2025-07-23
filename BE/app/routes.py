import requests
from flask import Blueprint, request, jsonify, send_file
from .gdrive import upload_file_to_drive, list_drive_files, delete_drive_file
from .services import generate_contract
import uuid

main = Blueprint('main', __name__)

@main.route('/ping')
def ping():
    return jsonify({"message": "pong"})


@main.route('/generate-contract', methods=['POST'])
def generate_contract_api():
    required_fields = [
        "agreement_date", "client_names", "service_providers",
        "project_title", "total_cost", "down_payment",
        "remaining_cost", "deadline_date"
    ]

    data = request.json

    # Validate required fields
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": "Missing fields", "fields": missing}), 400

    filename = f"contract_{uuid.uuid4().hex[:8]}.docx"
    path = generate_contract(data, filename)

    return send_file(path, as_attachment=True)


@main.route('/upload', methods=['POST'])
def upload():
    file = requests.files['file']
    if file:
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)
        file_id = upload_file_to_drive(file_path, file.filename, file.mimetype)
        return jsonify({"file_id": file_id}), 201
    return jsonify({"error": "No file uploaded"}), 400

@main.route('/files', methods=['GET'])
def files():
    files = list_drive_files()
    return jsonify(files), 200

@main.route('/delete/<file_id>', methods=['DELETE'])
def delete_file(file_id):
    delete_drive_file(file_id)
    return jsonify({"message": "File deleted"}), 200