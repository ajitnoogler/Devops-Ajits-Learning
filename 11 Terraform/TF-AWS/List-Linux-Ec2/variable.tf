variable "cidr_block" {
  description = "The CIDR block of world connecting vpc."
  type        = string
  default     = "0.0.0.0/0" # Allow all traffic (not recommended for production)

}