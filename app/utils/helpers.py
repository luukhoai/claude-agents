"""Helper utilities for file handling and other operations."""
import os
import uuid
from flask import current_app
from werkzeug.utils import secure_filename
from typing import Optional, Dict, Any, List


def generate_unique_filename(original_filename: str) -> str:
    """
    Generate a unique filename to prevent conflicts.

    Args:
        original_filename: Original name of the uploaded file

    Returns:
        Unique filename with UUID prefix
    """
    safe_filename = secure_filename(original_filename)
    return f"{uuid.uuid4()}_{safe_filename}"


def save_uploaded_file(file, upload_folder: str) -> Optional[Dict[str, Any]]:
    """
    Save an uploaded file to the designated folder.

    Args:
        file: File object from request
        upload_folder: Path to the upload directory

    Returns:
        Dictionary containing file info if successful, None otherwise
    """
    if not file or file.filename == '':
        return None

    unique_filename = generate_unique_filename(file.filename)
    file_path = os.path.join(upload_folder, unique_filename)
    file.save(file_path)

    return {
        'original_filename': secure_filename(file.filename),
        'stored_filename': unique_filename,
        'size': file.content_length,
        'type': file.content_type or 'application/octet-stream'
    }


def format_error_response(message: str, status_code: int = 400) -> tuple:
    """
    Format a standard error response.

    Args:
        message: Error message
        status_code: HTTP status code

    Returns:
        Tuple of (response_dict, status_code)
    """
    return {'success': False, 'error': message}, status_code


def format_success_response(data: Any, status_code: int = 200) -> tuple:
    """
    Format a standard success response.

    Args:
        data: Data to include in response
        status_code: HTTP status code

    Returns:
        Tuple of (response_dict, status_code)
    """
    return {'success': True, 'data': data}, status_code


# =============================================================================
# Contact Store Helper Functions
# =============================================================================

def get_contacts_store() -> List[Dict[str, Any]]:
    """Get the contacts store from the current app."""
    return current_app.config.get('CONTACTS_STORE', [])


def find_contact_by_id(contact_id: str) -> Optional[Dict[str, Any]]:
    """
    Find a contact by its ID.

    Args:
        contact_id: The ID of the contact to find

    Returns:
        Contact dict if found, None otherwise
    """
    contacts = get_contacts_store()
    for contact in contacts:
        if contact['id'] == contact_id:
            return contact
    return None


def find_contact_by_email(email: str) -> Optional[Dict[str, Any]]:
    """
    Find a contact by its email (case-insensitive).

    Args:
        email: Email address to search for

    Returns:
        Contact dict if found, None otherwise
    """
    email_lower = email.lower().strip()
    contacts = get_contacts_store()
    for contact in contacts:
        if contact['email'].lower().strip() == email_lower:
            return contact
    return None


def check_email_exists(email: str) -> bool:
    """
    Check if email already exists in contacts (case-insensitive).

    Args:
        email: Email to check

    Returns:
        True if email exists, False otherwise
    """
    return find_contact_by_email(email) is not None


def delete_contact_by_id(contact_id: str) -> bool:
    """
    Delete a contact by its ID.

    Args:
        contact_id: The ID of the contact to delete

    Returns:
        True if deleted, False if not found
    """
    contacts = get_contacts_store()
    original_count = len(contacts)
    contacts[:] = [c for c in contacts if c['id'] != contact_id]
    return len(contacts) < original_count
