import requests
import time
import sys

def check_ssl_Vulnerabilities(domain, output_file):
    with open(output_file, "w") as file:
        file.write(f"Scanned for Vulnerabilities and Grade for {domain}:\n\n")
        
        url = f"https://api.ssllabs.com/api/v3/analyze?host={domain}&all=done"
        
        while True:
            response = requests.get(url)
            data = response.json()
            status = data.get("status")

            if status == "READY":
                endpoints = data.get('endpoints', [])
                if endpoints:
                    endpoint = endpoints[0]
                    ip = endpoint.get('ipAddress')
                    grade = endpoint.get('grade', 'N/A')
                    file.write(f"Endpoint: {ip}, Grade: {grade}\n")
                    
                    vulnerabilities = {
                        'Heartbleed': endpoint.get('details', {}).get('heartbleed', False),
                        'Poodle': endpoint.get('details', {}).get('poodle', False),
                        'VulnBeast': endpoint.get('details', {}).get('vulnBeast', False),
                        'Freak': endpoint.get('details', {}).get('freak', False)
                    }

                    for vuln_name, is_vulnerable in vulnerabilities.items():
                        file.write(f"  {vuln_name}: {'Vulnerable' if is_vulnerable else 'Not Vulnerable'}\n")
                    file.write("\nScanned for incompatibilities...\n")
                    check_incompatibilities(endpoint, file)
                else:
                    file.write("No endpoints found.\n")
                break
            elif status == "ERROR":
                file.write(f"Error during SSL check for {domain}.\n")
                return
            else:
                print("Analysis in progress, please wait...")
                time.sleep(30)

def check_incompatibilities(endpoint, file):
    incompatible_clients = []
    results = endpoint.get('details', {}).get('sims', {}).get('results', [])
    for client in results:
        if client.get("errorCode", 0) != 0:
            client_info = f"{client.get('client', {}).get('name')} {client.get('client', {}).get('version')}"
            error_code = client.get("errorCode")
            incompatible_clients.append(f"{client_info}, Error Code: {error_code}")

    if incompatible_clients:
        file.write("Incompatible Clients:\n")
        for client in incompatible_clients:
            file.write(f"  {client}\n")
    else:
        file.write("No incompatibilities found. All clients compatible.\n")

def print_file_contents(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ssl_check.py <domain>")
        sys.exit(1)
    domain_to_check = sys.argv[1]
    output_file_path = "ssl_scan_results.txt"
    
    check_ssl_Vulnerabilities(domain_to_check, output_file_path)
    
    print_file_contents(output_file_path)
