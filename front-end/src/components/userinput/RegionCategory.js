import React, { useState } from 'react';
import './userinput.css'

const RegionCategory = ({handleCurrentRegionChange}) => {
    
    const [regionCategory1, setRegionCategory1] = useState("");
    const [regionCategory2, setRegionCategory2] = useState("");
    
    const handleRegionCategory1Change = (e) => {
        if(e.target.value === "00" || e.target.value === "30"){
            handleCurrentRegionChange(e)
        }
        setRegionCategory1(e.target.value)
    }

    const handleRegionCategory2Change = (e) => {
        handleCurrentRegionChange(e)
        setRegionCategory2(e.target.value)
    }


    return (
        <div style={{display:'flex', flexDirection:'row'}}>
            <select className='select' value={regionCategory1} onChange={handleRegionCategory1Change} style={{marginRight:"10px"}}>
                <option value="00">선택</option>
                <option value="10">서울</option>
                <option value="20">경기도</option>
                <option value="30">인천</option>
            </select>
            <select className='select' value={regionCategory2} onChange={handleRegionCategory2Change}>
                {regionCategory1 === "10" && (
                    <React.Fragment>
                        <option value="100">선택</option>
                        <option value="101">강남구</option>
                        <option value="102">강동구</option>
                        <option value="103">강북구</option>
                        <option value="104">강서구</option>
                        <option value="105">관악구</option>
                        <option value="106">광진구</option>
                        <option value="107">구로구</option>
                        <option value="108">금천구</option>
                        <option value="109">노원구</option>
                        <option value="110">도봉구</option>
                        <option value="111">동대문구</option>
                        <option value="112">동작구</option>
                        <option value="113">마포구</option>
                        <option value="114">서대문구</option>
                        <option value="115">서초구</option>
                        <option value="116">성동구</option>
                        <option value="117">성북구</option>
                        <option value="118">송파구</option>
                        <option value="119">양천구</option>
                        <option value="120">영등포구</option>
                        <option value="121">용산구</option>
                        <option value="122">은평구</option>
                        <option value="123">종로구</option>
                        <option value="124">중구</option>
                        <option value="125">중랑구</option>
                    </React.Fragment>
                )}
                {regionCategory1 === "20" && (
                    <React.Fragment>
                        <option value="200">선택</option>
                        <option value="201">가평군</option>
                        <option value="202">고양특례시</option>
                        <option value="203">과천시</option>
                        <option value="204">광명시</option>
                        <option value="205">광주시</option>
                        <option value="206">구리시</option>
                        <option value="207">군포시</option>
                        <option value="208">김포시</option>
                        <option value="209">남양주시</option>
                        <option value="210">동두천시</option>
                        <option value="211">부천시</option>
                        <option value="212">성남시</option>
                        <option value="213">수원특례시</option>
                        <option value="214">시흥시</option>
                        <option value="215">안산시</option>
                        <option value="216">안성시</option>
                        <option value="217">안양시</option>
                        <option value="218">양주시</option>
                        <option value="219">양평군</option>
                        <option value="220">여주시</option>
                        <option value="221">연천군</option>
                        <option value="222">오산시</option>
                        <option value="223">용인특례시</option>
                        <option value="224">의왕시</option>
                        <option value="225">의정부시</option>
                        <option value="226">이천시</option>
                        <option value="227">파주시</option>
                        <option value="228">평택시</option>
                        <option value="229">포천시</option>
                        <option value="230">하남시</option>
                        <option value="231">화성시</option>
                    </React.Fragment>
                )}
                {regionCategory1 === "30" && (
                    <React.Fragment>
                        <option value="300">해당사항없음</option>
                    </React.Fragment>
                )}
            </select>
        </div>
    );
};

export default RegionCategory;