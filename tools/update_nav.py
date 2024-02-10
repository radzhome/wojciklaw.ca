"""
Allows repetitive updates to the navbar section of the website

Run by executing the following:
cd tools
python3 update_nav.py
"""
from update_func import update_section

# Define the new navbar content
navbar = """
    <nav class="navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0">
        <a href="/" class="navbar-brand d-flex align-items-center px-4 px-lg-5">
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
                        <a href="services.html" class="dropdown-item">Our Services</a>
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
                        <a href="buyers-roadmap.html" class="dropdown-item">Buyer Roadmap</a>

                    </div>
                </div>

                <div class="nav-item dropdown">
                    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">sellers</a>
                    <div class="dropdown-menu fade-down m-0">
                        <a href="sellers-checklist.html" class="dropdown-item">Seller Checklist</a>
                        <a href="sellers-closing-costs.html" class="dropdown-item">Closing costs</a>
                        <a href="sellers-roadmap.html" class="dropdown-item">Seller Roadmap</a>
                    </div>
                </div>
                <a href="faq.html" class="nav-item nav-link">FAQ</a>
                <a href="contact.html" class="nav-item nav-link">Contact</a>

            </div>
            <a href="blog.html" class="btn btn-primary py-4 px-lg-5 d-none d-lg-block">Blog<i class="fa fa-arrow-right ms-3"></i></a>
        </div>
    </nav>
"""
update_section(section='Navbar', new_content=navbar)