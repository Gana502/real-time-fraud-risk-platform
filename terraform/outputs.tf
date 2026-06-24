output "api_service_name" {
  value = kubernetes_service.fraud_risk_api_service.metadata[0].name
}

output "api_deployment_name" {
  value = kubernetes_deployment.fraud_risk_api.metadata[0].name
}