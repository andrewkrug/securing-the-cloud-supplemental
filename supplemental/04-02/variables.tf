variable organization_root {
    default = "r-qmkp"
}

variable "attach_restrict_region_ous" {
  description = "Attach OUs to restrict_regions."
  type        = list(string)
  default     = [
    
  ]
}
