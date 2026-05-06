## Flask Cybersecurity Lab Server

This repository contains a Flask-based web server designed for use in a **cybersecurity laboratory environment**. While it is capable of running on any machine with Python, it is currently configured for the **Arduino Uno Q**. 

The server operates over **HTTP**, intentionally lacking encryption to facilitate the **interception of data** between the client and server. This setup is ideal for analyzing packet captures and studying man-in-the-middle (MITM) attack vectors within a controlled lab setting.

##Notes on Arduino Uno Q and this readme

The Arduino Uno Q runs a full Debian distro. This readme is built for a linux machine, though this program can also be run with any Python interpreter given that the correct libraries are installed. I usually run in VS Code on a Windows Machine during CI/CD.
---

### Installation and Setup

To maintain system integrity and avoid dependency conflicts, it is highly recommended to install the required libraries within a **Python virtual environment**.

1.  **Clone the repository** to your local machine.
2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
3.  **Install the dependencies**:
    ```bash
    pip install Flask Flask-SQLAlchemy gunicorn
    ```

### Running the Server

While the included `run.py` script can be used for quick testing, it utilizes the built-in Flask development server, which is not designed for stability or security. For a more robust hosting solution, it is recommended to use **Gunicorn** (Green Unicorn), a production-grade WSGI HTTP Server.

*   **To boot via the development script**:
    ```bash
    python run.py
    ```
*   **To host via Gunicorn**:
    ```bash
    gunicorn -w 4 -b 0.0.0.0:8000 run:app
    ```

---

### Technical Requirements

*   **Flask / Jinja2**: Core web framework and templating engine.
*   **Flask-SQLAlchemy**: Database abstraction and management.
*   **Gunicorn**: Recommended for stable server hosting.

### Lab Safety and Best Practices

*   **Network Isolation**: Because this server transmits data in cleartext (HTTP), ensure it is only run within a host-only or internal virtual network to prevent sensitive data exposure.
*   **Port Configuration**: Ensure your firewall allows traffic on the specific port designated in your `run.py` or Gunicorn command (defaulting to 5000 or 8000).
*   **Monitoring Tools**: This server is best paired with tools like **Wireshark** or **Tcpdump** to effectively capture and analyze the traffic generated during lab exercises.
```
