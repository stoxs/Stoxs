import React from 'react';

const Navbar = () => {
    return (
        <nav className="nav-wrapper">
            <div className="container">
                <a className="brand-logo">Stoxs</a>
                <ul className="right">
                    <li><a href="/nasdaqc">NASDAQ-C</a></li>
                    <li><a href="/nasdaqg">NASDAQ-G</a></li>
                    <li><a href="/nyse">NYSE</a></li>
                    <li><a href="/amex">AMEX</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </div>
        </nav>
    )
}

export default Navbar;