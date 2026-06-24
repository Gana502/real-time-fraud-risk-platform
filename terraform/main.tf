terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.35"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "fraud_risk_api" {
  metadata {
    name = "fraud-risk-api"

    labels = {
      app = "fraud-risk-api"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "fraud-risk-api"
      }
    }

    template {
      metadata {
        labels = {
          app = "fraud-risk-api"
        }
      }

      spec {
        container {
          name  = "fraud-risk-api"
          image = var.api_image

          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "fraud_risk_api_service" {
  metadata {
    name = "fraud-risk-api-service"
  }

  spec {
    selector = {
      app = "fraud-risk-api"
    }

    port {
      port        = 8000
      target_port = 8000
    }

    type = "ClusterIP"
  }
}