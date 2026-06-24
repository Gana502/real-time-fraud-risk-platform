variable "api_image" {
  description = "Docker image for the Fraud Risk API"
  type        = string
  default     = "ghcr.io/gana502/fraud-risk-api:latest"
}