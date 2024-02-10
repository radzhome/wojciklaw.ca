"""
Allows repetitive updates to the footer of the website

Run by executing the following:
cd tools
python3 update_footer.py
"""
from update_func import update_section

# Define the new content
footer = """
    <div class="container-fluid bg-dark text-light footer pt-5 mt-5 wow fadeIn" data-wow-delay="0.1s">
        <div class="container py-5">
            <div class="row g-5">
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-white mb-3">Quick Link</h4>
                    <a class="btn btn-link" href="about.html">About Us</a>
                    <a class="btn btn-link" href="contact.html">Contact Us</a>
                    <a class="btn btn-link" href="buyers-closing-costs.html">Buyers</a>
                    <a class="btn btn-link" href="sellers-closing-costs.html">Sellers</a>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4 class="text-white mb-3">Contact</h4>
                    <p class="mb-2"><i class="fa fa-map-marker-alt me-3"></i><a class="text-white" href="contact.html">201 Consumers Rd Unit 207</a></p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3 "></i><a class="text-white" href="tel:(416) 292-8277">(416) 292-8277</a></p>
                    <p class="mb-2"><i class="fa fa-phone-alt me-3 "></i>Fax (416) 292-8778</p>
                    <p class="mb-2"><i class="fa fa-envelope me-3"></i><a class="text-white" href="mailto:wojcikpc@gmail.com">wojcikpc@gmail.com</a></p>
                    <div class="d-flex pt-2">
                        <a class="btn btn-outline-light btn-social" href="https://www.linkedin.com/in/greg-wojcik-0aa28a127/" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>

                <div class="col-lg-3 col-md-6">
                    <h4 class="text-white mb-3">Share</h4>
                    <div class="row g-2 pt-2">
                        <ul class="social-network">
                        <span class='st_facebook' displayText=''></span>
                        <span class='st_twitter' displayText=''></span>
                        <span class='st_linkedin' displayText=''></span>
					</ul>
                    </div>
                </div>

            </div>
        </div>
        <div class="container">
            <div class="copyright">
                <div class="row">
                    <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                        &copy; <a class="border-bottom" href="#">WojcikLaw.ca</a>, 2024 All Right Reserved.

                    </div>
                    <div class="col-md-6 text-center text-md-end">
                        <div class="footer-menu">
                            <a href="/">Home</a>
                            <a href="about.html">About</a>
                            <a href="services.html">Services</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""
update_section(section='Footer', new_content=footer)