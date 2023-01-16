# Copyright (c) 2023, ithead@ambibuzz.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


from base64 import b64encode
from io import BytesIO 

import qrcode
class TexttoQRcode(Document):
	pass




@frappe.whitelist()
def generate_qr_code(qr_code_text):
	qr_code_base64 = get_qr_code(qr_code_text)
	return qr_code_base64



def get_qr_code(data: str) -> str:
	qr_code_bytes = get_qr_code_bytes(data, format="PNG")
	base_64_string = bytes_to_base64_string(qr_code_bytes)

	return add_file_info(base_64_string)


def add_file_info(data: str) -> str:
	"""Add info about the file type and encoding.
	
	This is required so the browser can make sense of the data."""
	return f"data:image/png;base64, {data}"


def get_qr_code_bytes(data, format: str) -> bytes:
	"""Create a QR code and return the bytes."""
	img = qrcode.make(data)

	buffered = BytesIO()
	img.save(buffered, format=format)

	return buffered.getvalue()


def bytes_to_base64_string(data: bytes) -> str:
	"""Convert bytes to a base64 encoded string."""
	return b64encode(data).decode("utf-8")