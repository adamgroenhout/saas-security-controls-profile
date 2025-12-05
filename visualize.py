import tomllib
import json
import datetime

# --- Constants ---
INPUT_FILE = "sscp-template.toml"
MARKDOWN_FILE = "SSCP_VISUALIZATION.md"
HTML_FILE = "SSCP_VISUALIZATION.html"

# --- HTML Template ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSCP Configuration Dashboard</title>
    <style>
        :root {{
            --primary: #2563eb;
            --success: #16a34a;
            --danger: #dc2626;
            --warning: #ca8a04;
            --bg: #f3f4f6;
            --card-bg: #ffffff;
            --text: #1f2937;
            --text-muted: #6b7280;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max_width: 1200px;
            margin: 0 auto;
        }}
        header {{
            background-color: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        h1 {{ margin: 0; font-size: 1.5rem; }}
        .meta-info {{ font-size: 0.9rem; color: var(--text-muted); }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: var(--card-bg);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .stat-value {{ font-size: 2rem; font-weight: bold; color: var(--primary); }}
        .stat-label {{ font-size: 0.9rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }}

        .section-title {{
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e5e7eb;
            font-size: 1.25rem;
            color: var(--text);
            text-transform: capitalize;
        }}

        .controls-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }}

        .control-card {{
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            padding: 20px;
            border-left: 4px solid var(--primary);
            transition: transform 0.2s;
        }}
        .control-card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}

        .control-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }}
        .control-name {{ font-weight: bold; font-size: 1.1rem; }}
        .status-badge {{
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 600;
        }}
        .status-enabled {{ background: #dcfce7; color: var(--success); }}
        .status-disabled {{ background: #fee2e2; color: var(--danger); }}

        .control-desc {{ font-size: 0.9rem; color: var(--text-muted); margin-bottom: 15px; line-height: 1.4; }}

        .control-details {{
            background: #f9fafb;
            padding: 10px;
            border-radius: 4px;
            font-size: 0.85rem;
        }}
        .detail-row {{ display: flex; justify-content: space-between; margin-bottom: 5px; }}
        .detail-label {{ font-weight: 600; color: var(--text-muted); }}
        .detail-value {{ font-family: monospace; color: var(--primary); }}

        .exception-flag {{
            margin-top: 10px;
            padding: 5px;
            background: #fef3c7;
            color: var(--warning);
            font-size: 0.8rem;
            border-radius: 4px;
            text-align: center;
        }}

        /* Integration Apps Styling */
        .app-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 10px;
            margin-top: 10px;
        }}
        .app-item {{
            background: white;
            border: 1px solid #e5e7eb;
            padding: 8px;
            border-radius: 4px;
        }}

    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>{app_name}</h1>
                <div class="meta-info">SSCP Security Configuration Baseline</div>
            </div>
            <div style="text-align: right">
                <div class="meta-info">Generated: {date}</div>
                <div class="meta-info">Version: {version}</div>
            </div>
        </header>

        <div class="summary-grid">
            <div class="stat-card">
                <div class="stat-value">{total_controls}</div>
                <div class="stat-label">Total Controls</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{enabled_controls}</div>
                <div class="stat-label">Enabled</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{exceptions_count}</div>
                <div class="stat-label">Exceptions</div>
            </div>
        </div>

        {content}

    </div>
</body>
</html>
"""

def load_data():
    with open(INPUT_FILE, "rb") as f:
        return tomllib.load(f)

def is_control(data):
    """Check if a dictionary looks like a control definition."""
    if not isinstance(data, dict):
        return False
    # Heuristic: Controls usually have 'description', 'relevant', 'enabled'
    return 'description' in data and 'relevant' in data and 'enabled' in data

def generate_markdown(data):
    lines = ["# SSCP Configuration Report", "", f"**Generated:** {datetime.date.today()}", ""]

    # Meta Info
    meta = data.get("meta", {}).get("application", {})
    lines.append(f"**Application:** {meta.get('name', 'N/A')}")
    lines.append(f"**Description:** {meta.get('description', 'N/A')}")
    lines.append("")

    for section_name, section_data in data.items():
        if section_name == "meta":
            continue

        lines.append(f"## {section_name.upper()}")
        lines.append("| Control | Enabled | Value | Exception | Description |")
        lines.append("| :--- | :---: | :--- | :---: | :--- |")

        for key, value in section_data.items():
            if is_control(value):
                enabled = "✅" if value.get("enabled") else "❌"
                val = value.get("value", "")

                # Special handling for connected_apps which doesn't have a simple 'value' usually
                if key == "connected_apps":
                    val = "[See Details]"
                elif isinstance(val, list):
                    val = ", ".join(val)

                exception = "⚠️" if value.get("exception") else "-"
                desc = value.get("description", "").split(".")[0] + "." # First sentence

                lines.append(f"| {key} | {enabled} | `{val}` | {exception} | {desc} |")

                # If it's connected_apps, maybe list sub-items in a separate small table or list?
                # For Markdown table simplicity, we might skip deep detail, but let's see.
                if key == "connected_apps":
                    # Check for sub-tables (apps)
                    apps = [k for k, v in value.items() if isinstance(v, dict)]
                    if apps:
                        # Add a row for the apps maybe? Or just leave it.
                        pass
        lines.append("")

    return "\n".join(lines)

def generate_html(data):
    meta_app = data.get("meta", {}).get("application", {})
    meta_template = data.get("meta", {}).get("template", {})

    app_name = meta_app.get("name", "Unknown App")
    version = meta_template.get("sscp_template_version", "0.0")

    sections_html = ""

    total_controls = 0
    enabled_controls = 0
    exceptions_count = 0

    for section_name, section_data in data.items():
        if section_name == "meta":
            continue

        section_html = f'<div class="section-title">{section_name}</div><div class="controls-grid">'

        for key, value in section_data.items():
            if is_control(value):
                total_controls += 1
                is_enabled = value.get("enabled", False)
                if is_enabled:
                    enabled_controls += 1
                if value.get("exception"):
                    exceptions_count += 1

                status_class = "status-enabled" if is_enabled else "status-disabled"
                status_text = "ENABLED" if is_enabled else "DISABLED"

                val = value.get("value", "N/A")
                if isinstance(val, list):
                    val = ", ".join(val)

                # Special handling for configuration_details dict
                config_details = value.get("configuration_details", "")
                config_html = ""
                if isinstance(config_details, dict):
                    for k, v in config_details.items():
                        config_html += f'<div class="detail-row"><span class="detail-label">{k}:</span> <span class="detail-value">{v}</span></div>'

                # Special handling for connected_apps (sub-items)
                sub_items_html = ""
                if key == "connected_apps":
                    val = "Multiple Apps"
                    for sub_key, sub_val in value.items():
                        if isinstance(sub_val, dict):
                            # It's an app
                            sub_items_html += f"""
                            <div class="app-item">
                                <strong>{sub_key}</strong><br>
                                <span style="font-size:0.8em">Type: {sub_val.get('account_type')} | Rotation: {sub_val.get('credential_rotation')}</span>
                            </div>
                            """
                    if sub_items_html:
                        sub_items_html = f'<div class="app-grid">{sub_items_html}</div>'


                card_html = f"""
                <div class="control-card">
                    <div class="control-header">
                        <div class="control-name">{key}</div>
                        <div class="status-badge {status_class}">{status_text}</div>
                    </div>
                    <div class="control-desc">{value.get("description", "")}</div>
                    <div class="control-details">
                        <div class="detail-row">
                            <span class="detail-label">Value:</span>
                            <span class="detail-value">{val}</span>
                        </div>
                        {config_html}
                    </div>
                    {sub_items_html}
                    {f'<div class="exception-flag">⚠️ Exception Granted: {value.get("exception_id")}</div>' if value.get("exception") else ''}
                </div>
                """
                section_html += card_html

        section_html += "</div>"
        sections_html += section_html

    return HTML_TEMPLATE.format(
        app_name=app_name,
        date=datetime.date.today(),
        version=version,
        total_controls=total_controls,
        enabled_controls=enabled_controls,
        exceptions_count=exceptions_count,
        content=sections_html
    )

def main():
    try:
        data = load_data()

        # Generate Markdown
        md_content = generate_markdown(data)
        with open(MARKDOWN_FILE, "w") as f:
            f.write(md_content)
        print(f"Generated {MARKDOWN_FILE}")

        # Generate HTML
        html_content = generate_html(data)
        with open(HTML_FILE, "w") as f:
            f.write(html_content)
        print(f"Generated {HTML_FILE}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
