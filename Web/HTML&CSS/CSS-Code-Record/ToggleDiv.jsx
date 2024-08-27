import React, { useState } from 'react';
import styled from "styled-components";

const StyledToggleDiv = styled.div`
    width: 100%;
`;

const ToggleContent = styled.div`
    height: ${props => props.isVisible ? '120px' : '0'};
    overflow: scroll;
    transition: height 0.3s;
    
    /* Hide horizontal and vertical scroll bars  */
    &::-webkit-scrollbar {
        display: none;  
    }
    -ms-overflow-style: none; 
    scrollbar-width: none;  
`;

const ToggleButton = styled.button`
    display: block;
    border: none;
    background-color: white;
`;

const ToggleDiv = ({ children, ...props }) => {
    const [isVisible, setIsVisible] = useState();

    return (
        <StyledToggleDiv>
            <ToggleButton onClick={() => setIsVisible(!isVisible)} >
                {props.name}
            </ToggleButton>
            <ToggleContent isVisible={isVisible} >
                {children}
            </ToggleContent>
        </StyledToggleDiv>
    );
};

export default ToggleDiv;