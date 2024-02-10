"""
Run by executing the following:
    python3 update_section.py
"""
import os
import re

# Define the directory where your HTML files are located
directory = '../'

# Define the new navbar content
navbar = """
    <nav class="navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0">
        <a href="index.html" class="navbar-brand d-flex align-items-center px-4 px-lg-5">
            <img class="navbar-logo" src="/img/wojcik.png">Wojcik Law
        </a>
        <button type="button" class="navbar-toggler me-4" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <div class="navbar-nav ms-auto p-4 p-lg-0">
                <a href="index.html" class="nav-item nav-link active">Home</a>
                <a href="about.html" class="nav-item nav-link">About</a>

                <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">services</a>
                    <div class="dropdown-menu fade-down m-0">
                        <a href="services.html" class="dropdown-item">Services</a>
                        <a href="services-commercial.html" class="dropdown-item">Commercial</a>
                        <a href="services-family-law.html" class="dropdown-item">Family Law</a>
                        <a href="services-real-estate.html" class="dropdown-item">Real Estate</a>
                        <a href="services-wills-estates.html" class="dropdown-item">Wills & Estates</a>
                    </div>
                </div>


                <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">buyers</a>
                    <div class="dropdown-menu fade-down m-0">
                        <a href="buyers-closing-costs.html" class="dropdown-item">Closing costs</a>
                        <a href="buyers-closing-day.html" class="dropdown-item">Closing Day</a>
                        <a href="buyers-condominiums.html" class="dropdown-item">Condominiums</a>
                        <a href="buyers-land-transfer-tax.html" class="dropdown-item">Land Transfer Tax</a>
                        <a href="buyers-mortgage-calculator.html" class="dropdown-item">Mortgage Calculator</a>
                        <a href="buyers-roadmap.html" class="dropdown-item">Road map</a>

                    </div>
                </div>

                <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">sellers</a>
                    <div class="dropdown-menu fade-down m-0">
                        <a href="sellers-checklist.html" class="dropdown-item">Checklist</a>
                        <a href="sellers-closing-costs.html" class="dropdown-item">Closing costs</a>
                        <a href="sellers-roadmap.html" class="dropdown-item">Roadmap</a>
                    </div>
                </div>
                <a href="faq.html" class="nav-item nav-link">FAQ</a>
                <a href="contact.html" class="nav-item nav-link">Contact</a>

            </div>
            <a href="blog.html" class="btn btn-primary py-4 px-lg-5 d-none d-lg-block">Blog<i class="fa fa-arrow-right ms-3"></i></a>
        </div>
    </nav>
"""

# Iterate over all HTML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        with open(os.path.join(directory, filename), 'r') as file:
            file_content = file.read()

        # Replace the navbar content in each file with the new navbar content
        file_content = re.sub('<!-- Navbar Start -->.*<!-- Navbar End -->', navbar, file_content, flags=re.DOTALL)

        # Write the updated content back to the file
        with open(os.path.join(directory, filename), 'w') as file:
            file.write(file_content)