provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "kind-kind-java"
}

resource "kubernetes_deployment_v1" "java_app" {
  metadata {
    name      = "java-deployment"
    namespace = "kind-java"
    labels = {
      app = "example-app"
    }
  }

  spec {
    replicas = 2 # Adjusted replicas count

    selector {
      match_labels = {
        app = "example-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "example-app"
        }
      }

      spec {
        container {
          name  = "java-app-container"
          image = "nginx:latest"

          resources {
            limits = {
              memory = "128Mi"
              cpu    = "500m"
            }
            requests = {
              memory = "64Mi"
              cpu    = "250m"
            }
          }

          port {
            container_port = 8080
          }
        }
      }
    }
  }
}

# Blue Deployment
resource "kubernetes_deployment_v1" "java_app_blue" {
  metadata {
    name      = "java-deployment-blue"
    namespace = "kind-java"
    labels = {
      app = "example-app"
      env = "blue"
    }
  }

  spec {
    replicas = 3 # Adjusted replicas count

    selector {
      match_labels = {
        app = "example-app"
        env = "blue"
      }
    }

    template {
      metadata {
        labels = {
          app = "example-app"
          env = "blue"
        }
      }

      spec {
        container {
          name  = "java-app-container"
          image = "nginx:latest"

          resources {
            limits = {
              memory = "128Mi"
              cpu    = "500m"
            }
            requests = {
              memory = "64Mi"
              cpu    = "250m"
            }
          }

          port {
            container_port = 8080
          }
        }
      }
    }
  }
}

# Green Deployment
resource "kubernetes_deployment_v1" "java_app_green" {
  metadata {
    name      = "java-deployment-green"
    namespace = "kind-java"
    labels = {
      app = "example-app"
      env = "green"
    }
  }

  spec {
    replicas = 2 # Adjusted replicas count

    selector {
      match_labels = {
        app = "example-app"
        env = "green"
      }
    }

    template {
      metadata {
        labels = {
          app = "example-app"
          env = "green"
        }
      }

      spec {
        container {
          name  = "java-app-container"
          image = "nginx:latest"

          resources {
            limits = {
              memory = "128Mi"
              cpu    = "500m"
            }
            requests = {
              memory = "64Mi"
              cpu    = "250m"
            }
          }

          port {
            container_port = 8080
          }
        }
      }
    }
  }
}

# Load Balancer Service
resource "kubernetes_service_v1" "java_app_lb" {
  metadata {
    name      = "java-app-lb"
    namespace = "kind-java"
  }

  spec {
    selector = {
      app = "example-app"
      env = "blue" # Initially route traffic to blue
    }

    port {
      protocol    = "TCP"
      port        = 8080
      target_port = 8080
    }

    type = "LoadBalancer"
  }
}