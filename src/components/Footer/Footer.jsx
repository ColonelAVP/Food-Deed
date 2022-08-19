import React from 'react'
import { Container, Row, Col, ListGroup, ListGroupItem } from "reactstrap"
import logo from '../../assets/images/res-logo.png'
import {Link} from "react-router-dom"

import '../../styles/footer.css'
function Footer() {
    return (
        <footer className='footer'>
            <Container>
                <Row>
                    <Col lg='3' md='4' sm='6'>
                        <div className="footer_logo text-start">
                            <img src={logo} alt="logo" />
                            <h5 className='footer-title'>Food deed</h5>
                            <p>
                                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                                Neque maiores obcaecati, alias eius, est provident praesentium perspiciatis voluptatum voluptatem suscipit amet.
                            </p>
                        </div>
                    </Col>
                    <Col lg='3' md='4' sm='6'>
                        <h5 className='footer-title'>Delivery Time</h5>
                        <ListGroup className='deliver_item-list'>
                            <ListGroupItem className='delivery_time-item border-0 ps-0'>
                                <span>Sunday - Thursday</span>
                                <p>10:00am - 11:00pm</p>
                            </ListGroupItem>

                            <ListGroupItem className='delivery_time-item border-0 ps-0'>
                                <span>Friday - Saturday</span>
                                <p>Off day</p>
                            </ListGroupItem>
                        </ListGroup>
                    </Col>
                    <Col lg='3' md='4' sm='6'>
                        <h5 className='footer-title'>Contact</h5>
                        <ListGroup className='deliver_item-list'>
                        <ListGroupItem className='delivery_time-item border-0 ps-0'>
                                <p>Location: Colaba Market, Mumbai-400005, Maharashtra, India </p>
                            </ListGroupItem>
                            <ListGroupItem className='delivery_time-item border-0 ps-0'>
                                <span>Phone: +91XXXXXX63 </span>
                            </ListGroupItem>
                            <ListGroupItem className='delivery_time-item border-0 ps-0'>
                                <span>Email: example@gmail.com</span>
                            </ListGroupItem>
                        </ListGroup>
                    </Col>
                    <Col lg='3' md='4' sm='6'>
                    <h5 className='footer-title'>Newsletter</h5>
                    <p>Subsribe our newsletter</p>
                    <div className="newsletter">
                        <input type="email" placeholder="Enter yout email"/>
                        <span><i class="ri-send-plane-fill"></i></span>
                    </div>
                    </Col>
                </Row>
                <Row className='mt-4'>
                    <Col lg='6' md='6'>
                        <p className='copyright_text'>Copyright - 2022, website made by Sachin kumawat and Atherv patil. All Rights Reserved</p> 
                    </Col>
                    <Col lg='6' md='6'> 
                        <div className="social_links d-flex align-items-center gap-4 justify-content-end">
                         <p className='m-0'>Follow: </p>  
                         <span>{" "}<Link to=' ' ><i class="ri-facebook-circle-fill"></i></Link></span> 
                         <span><Link to=' '></Link><i class="ri-github-fill"></i></span>
                         <span>{" "}<Link to=' '></Link><i class="ri-linkedin-box-fill"></i></span>
                        </div>
                    </Col>
                </Row>
            </Container>
        </footer>)
}

export default Footer