import React, { useEffect, useState } from 'react'
import './recommendElement.css'

const RecommendElement = ({item}) => {

    const [loanPrice, setLoanPrice] = useState("");

    useEffect(()=>{
        getLoanPrice();
    },[item])

    const getLoanPrice = () => {
        if(item.loan === 0){
            setLoanPrice("필요없음")
        } else {
            setLoanPrice(`${item.loan}만원`)
        }
    }

    return (
        <div className = 'recommend_element_background'>
            <div className='recommend_element_title'>
                {item.name} {item.floor}층
            </div>
            <div className='recommend_element_text'>
                {item.addr} 
            </div>
            <div className='recommend_element_text'>
                실거래가 : {item.price}만원, 평수 : {item.size}평
            </div>
            <div className='recommend_element_text'>
                대출 : {loanPrice}
            </div>
        </div>
    );
};

export default RecommendElement;