import os
from datetime import datetime

class ReportWriter:
    def __init__(self, test_name):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Get absolute path to the project root (two levels up from this file)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Define logs directory outside multi_browser and report_creator
        logs_dir = os.path.join(project_root, "logs")
        os.makedirs(logs_dir, exist_ok=True)

        # Final report path
        self.report_path = os.path.join(logs_dir, f"{test_name}_{timestamp}.html")
        self.entries = []

    def log(self, status, message):
        self.entries.append((status.upper(), message))

    def generate(self):
        with open(self.report_path, "w", encoding="utf-8") as f:
            f.write("<html><head><title>Test Report</title></head><body>")
            f.write("<h2>Test Execution Report</h2><table border='1'>")
            f.write("<tr><th>Status</th><th>Message</th></tr>")
            
            for status, message in self.entries:
                if status == "PASS":
                    color = "green"
                elif status == "FAIL":
                    color = "red"
                elif status == "INFO":
                    color = "blue"
                else:
                    color = "yellow"
                
                f.write(f"<tr><td style='color:{color}'>{status}</td><td>{message}</td></tr>")
            
            f.write("</table></body></html>")
        
        print(f"✅ Report generated: {self.report_path}")