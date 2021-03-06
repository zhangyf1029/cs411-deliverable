import React from 'react'
import {Nav,NavLink,Bars,NavMenu,NavBtn,NavBtnLink} from './NavbarElements'
const Navbar = () => {
    return (
        <>
            <Nav>
                <NavLink to = "/">
                </NavLink>
                <Bars />
                <NavMenu>
                    <NavLink to = "/about" activeStyle>
                        About
                    </NavLink>
                    <NavLink to = "/start" activeStyle>
                        Start Matching
                    </NavLink>
                    <NavLink to = "/contact" activeStyle>
                        Contact Us
                    </NavLink>
                    <NavLink to = "/signup" activeStyle>
                        Sign Up
                    </NavLink>
                    <NavBtnLink to ="/signin"> Sign In </NavBtnLink>
                </NavMenu>
            </Nav>
            
        </>
    )
}

export default Navbar
