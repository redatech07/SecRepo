import re

SECRET_KEYWORDS = {

    # 1. Passwords and authentication
    "PASSWORD": [
        "password",
        "passwd",
        "pwd",
        "passphrase",
        "user_password",
        "admin_password",
        "root_password",
        "login_password",
        "default_password",
    ],

    # 2. API keys
    "API_KEY": [
        "api_key",
        "apikey",
        "api-key",
        "api_secret_key",
        "api_access_key",
        "public_api_key",
        "private_api_key",
        "api_token",
    ],

    # 3. Authentication tokens
    "TOKEN": [
        "token",
        "access_token",
        "refresh_token",
        "auth_token",
        "authentication_token",
        "bearer_token",
        "id_token",
        "jwt_token",
        "session_token",
        "personal_access_token",
    ],

    # 4. Application secrets
    "SECRET": [
        "secret",
        "client_secret",
        "app_secret",
        "application_secret",
        "signing_secret",
        "encryption_secret",
        "webhook_secret",
        "shared_secret",
        "consumer_secret",
    ],

    # 5. Private keys and cryptographic material
    "PRIVATE_KEY": [
        "private_key",
        "privatekey",
        "rsa_private_key",
        "ssh_private_key",
        "ec_private_key",
        "dsa_private_key",
        "encryption_key",
        "signing_key",
        "secret_key",
        "master_key",
        "root_key",
        "decrypt_key",
    ],

    # 6. Database credentials
    "DATABASE_CREDENTIALS": [
        "db_password",
        "database_password",
        "db_pass",
        "database_pass",
        "db_user",
        "database_user",
        "db_username",
        "database_username",
        "db_connection",
        "database_url",
        "database_uri",
        "connection_string",
        "connection_url",
        "mongodb_uri",
        "postgres_url",
        "mysql_password",
        "redis_password",
    ],

    # 7. AWS credentials
    "AWS_CREDENTIALS": [
        "aws_access_key_id",
        "aws_secret_access_key",
        "aws_session_token",
        "aws_security_token",
        "aws_credentials",
    ],

    # 8. Google Cloud credentials
    "GCP_CREDENTIALS": [
        "google_application_credentials",
        "google_cloud_key",
        "gcp_service_account",
        "gcp_credentials",
        "google_api_key",
    ],

    # 9. Azure credentials
    "AZURE_CREDENTIALS": [
        "azure_client_secret",
        "azure_client_id",
        "azure_tenant_id",
        "azure_storage_key",
        "azure_connection_string",
    ],

    # 10. Git provider credentials
    "GIT_CREDENTIALS": [
        "github_token",
        "github_pat",
        "gitlab_token",
        "gitlab_access_token",
        "bitbucket_token",
        "git_credentials",
        "git_access_token",
    ],

    # 11. SSH credentials
    "SSH_CREDENTIALS": [
        "ssh_password",
        "ssh_private_key",
        "ssh_key",
        "ssh_passphrase",
        "authorized_keys",
    ],

    # 12. Certificates
    "CERTIFICATES": [
        "private_certificate",
        "client_certificate",
        "ssl_certificate",
        "tls_certificate",
        "certificate_key",
        "cert_password",
        "keystore_password",
        "truststore_password",
    ],

    # 13. Payment services
    "PAYMENT_CREDENTIALS": [
        "stripe_secret_key",
        "stripe_api_key",
        "paypal_client_secret",
        "payment_secret",
        "payment_api_key",
        "merchant_secret",
    ],

    # 14. Communication services
    "COMMUNICATION_CREDENTIALS": [
        "slack_token",
        "slack_bot_token",
        "slack_webhook_url",
        "discord_token",
        "discord_webhook_url",
        "twilio_auth_token",
        "sendgrid_api_key",
        "mailgun_api_key",
    ],

    # 15. Encryption and signing
    "CRYPTOGRAPHIC_SECRETS": [
        "encryption_password",
        "encryption_key",
        "decryption_key",
        "aes_key",
        "rsa_key",
        "hmac_key",
        "signing_secret",
        "jwt_secret",
        "fernet_key",
    ],

    # 16. Infrastructure and deployment
    "INFRASTRUCTURE_CREDENTIALS": [
        "docker_password",
        "registry_password",
        "registry_token",
        "kubernetes_token",
        "kubeconfig",
        "terraform_token",
        "deploy_token",
        "deployment_key",
        "ci_token",
        "cd_token",
    ],

    # 17. Generic credentials
    "CREDENTIALS": [
        "credentials",
        "credential",
        "client_credentials",
        "service_account_key",
        "service_account_credentials",
        "auth_credentials",
        "login_credentials",
        "access_credentials",
    ],
}


def detect_keyword_secrets(content):

    findings = []

    for line_number, line in enumerate(content.splitlines(), start=1):

        normalized_line = line.lower()

        for category, keywords in SECRET_KEYWORDS.items():

            for keyword in keywords:

                if keyword in normalized_line:

                    findings.append({
                        "line": line_number,
                        "type": category,
                        "keyword": keyword
                    })

                    break

    return findings
