"""Security showcase — INTENTIONAL bandit/semgrep findings across all 7 SAST categories.

DO NOT USE ANY OF THIS CODE. Every function here exists to be flagged.
"""

import hashlib
import os
import pickle
import subprocess
import tempfile
import xml.etree.ElementTree as ET  # XXE-prone parser

import requests
import yaml
from flask import Flask
from jinja2 import Environment


# ---------------------------------------------------------------------------
# Hardcoded secrets — bandit B105/B106, sensitive_information_tracking
# ---------------------------------------------------------------------------
PASSWORD = "admin123"
API_KEY = "sk-test-aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
SECRET_TOKEN = "super-secret-please-rotate"
DB_USER = "root"
DB_PASS = "hunter2"


# ---------------------------------------------------------------------------
# Code-injection / RCE surface — bandit B307, B102, B602, B605
# ---------------------------------------------------------------------------
def dangerous_eval(expr):
    """Evaluate arbitrary expression (BAD: eval)."""
    return eval(expr)  # noqa: S307 — exploit_surface_identification


def dangerous_exec(snippet):
    """Execute arbitrary statements (BAD: exec)."""
    exec(snippet)  # noqa: S102 — exploit_surface_identification


def run_dangerous_shell(cmd):
    """Run a command via shell=True (BAD)."""
    return subprocess.run(cmd, shell=True, check=False)  # noqa: S602


def legacy_system(cmd):
    """Run a command via os.system (BAD)."""
    return os.system(cmd)  # noqa: S605


# ---------------------------------------------------------------------------
# Deserialization — bandit B301, B506
# ---------------------------------------------------------------------------
def unsafe_pickle_load(data):
    """Unpickle arbitrary bytes (BAD)."""
    return pickle.loads(data)  # noqa: S301


def unsafe_yaml_parse(s):
    """Parse YAML without SafeLoader (BAD)."""
    return yaml.load(s)  # noqa: S506 — no Loader


# ---------------------------------------------------------------------------
# TLS / HTTP misuse — bandit B501, regulatory_alignment
# ---------------------------------------------------------------------------
def insecure_get(url):
    """HTTPS without certificate verification (BAD)."""
    return requests.get(url, verify=False, timeout=5)  # noqa: S501


# ---------------------------------------------------------------------------
# Weak hashes — bandit B303/B324
# ---------------------------------------------------------------------------
def weak_md5_hash(data):
    """MD5 — broken hash (BAD)."""
    return hashlib.md5(data.encode()).hexdigest()  # noqa: S324


def weak_sha1_hash(data):
    """SHA1 — broken hash (BAD)."""
    return hashlib.sha1(data.encode()).hexdigest()  # noqa: S324


# ---------------------------------------------------------------------------
# Template injection — Jinja2 with autoescape disabled
# ---------------------------------------------------------------------------
def render_unsafe_template(template_str, ctx):
    """Render Jinja2 template with autoescape=False (BAD)."""
    env = Environment(autoescape=False)  # noqa: S701
    return env.from_string(template_str).render(**ctx)


# ---------------------------------------------------------------------------
# SQL injection — string-formatted query passed to cursor.execute
# ---------------------------------------------------------------------------
def build_query(uid):
    """Build SQL via f-string (BAD: SQLi)."""
    return f"SELECT * FROM users WHERE id={uid}"  # noqa: S608


def fetch_user(cursor, uid):
    """Execute string-formatted SQL (BAD)."""
    query = f"SELECT * FROM users WHERE id={uid}"  # noqa: S608
    cursor.execute(query)
    return cursor.fetchone()


# ---------------------------------------------------------------------------
# Insecure server defaults — debug=True + bind to all interfaces
# ---------------------------------------------------------------------------
def start_server():
    """Run Flask in debug mode bound to 0.0.0.0 (BAD)."""
    app = Flask(__name__)

    @app.route("/")
    def index():  # pragma: no cover
        return "hello"

    app.run(host="0.0.0.0", port=5000, debug=True)  # noqa: S104,S201


# ---------------------------------------------------------------------------
# Insecure tempfile — bandit B306
# ---------------------------------------------------------------------------
def make_temp():
    """tempfile.mktemp is race-prone (BAD)."""
    return tempfile.mktemp()  # noqa: S306


# ---------------------------------------------------------------------------
# XML XXE — bandit B314/B405
# ---------------------------------------------------------------------------
def parse_xml(payload):
    """Parse XML via stdlib ElementTree (XXE-prone)."""
    return ET.fromstring(payload)  # noqa: S314


def parse_xml_file(path):
    """Parse XML file via stdlib ElementTree (XXE-prone)."""
    return ET.parse(path)  # noqa: S314


# ---------------------------------------------------------------------------
# assert for security — bandit B101
# ---------------------------------------------------------------------------
def assert_admin(user):
    """Use assert as authz (BAD: stripped under -O)."""
    assert user.get("is_admin"), "not admin"  # noqa: S101
    return True
