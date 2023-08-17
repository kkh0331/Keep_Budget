import React, { useState } from 'react'
import '../components/userinput/userinput.css'
import RegionCategory from '../components/userinput/RegionCategory';
import AppHeader from '../components/common/AppHeader';
import { useNavigate } from 'react-router-dom';

const UserInputPage = () => {

    const [userName, setUserName] = useState("");
    const [annualIncome, setAnnualIncome] = useState(0);
    const [saveAmount, setSaveAmount] = useState(0);
    const [currentRegion, setCurrentRegion] = useState("");
    const [currentHouseType, setCurrentHouseType] = useState("");
    const [currentHousePrice, setCurrentHousePrice] = useState(0);
    const [totalAmount, setTotalAmount] = useState(0);
    const [loanAmount, setLoanAmount] = useState(0);
    const [averageMonthlyExpenditure, setAverageMonthlyExpenditure] = useState(0);

    const [moveDate, setMoveDate] = useState(0);
    const [moveRegion, setMoveRegion] = useState("");
    const [moveHouse, setMoveHouse] = useState("");
    const [moveHouseType, setMoveHouseType] = useState("");
    const [moveSize, setMoveSize] = useState(0);

    const navigate = useNavigate();

    const handleUserNameChange = (e) => {
        setUserName(e.target.value);
    }

    const handleAnnualIncomeChange = (e) => {
        setAnnualIncome(e.target.value);
    }

    const handleSaveAmountChange = (e) => {
        const value = parseInt(e.target.value);
        if(isNaN(value)){
            setSaveAmount(0);
            calculateTotalAmount(0,currentHousePrice,loanAmount);
        } else {
            setSaveAmount(value);
            calculateTotalAmount(value,currentHousePrice,loanAmount);
        }
    }

    const handleCurrentRegionChange = (e) => {
        setCurrentRegion(e.target.value);
    }

    const handleCurrentHouseTypeChange = (e) =>{
        setCurrentHouseType(e.target.value);
    }

    const handleCurrentHousePriceChange = (e) => {
        const value = parseInt(e.target.value);
        if(isNaN(value)){
            setCurrentHousePrice(0);
            calculateTotalAmount(saveAmount,0,loanAmount);
        } else {
            setCurrentHousePrice(value);
            calculateTotalAmount(saveAmount,value,loanAmount);
        }
    };

    const handleLoanAmountChange = (e) => {
        const value = parseInt(e.target.value);
        if(isNaN(value)){
            setLoanAmount(0);
            calculateTotalAmount(saveAmount,currentHousePrice,0);
        } else {
            setLoanAmount(value);
            calculateTotalAmount(saveAmount,currentHousePrice,value);
        }
    };

    const handleAverageMonthlyExpenditureChange = (e) => {
        setAverageMonthlyExpenditure(e.target.value);
    };

    const handleMoveDateChange = (e) => {
        setMoveDate(e.target.value);
    };

    const handleMoveRegionChange = (e) => {
        setMoveRegion(e.target.value);
    }

    const handleMoveHouseChange = (e) => {
        setMoveHouse(e.target.value);
    }

    const handleMoveHouseTypeChange = (e) => {
        setMoveHouseType(e.target.value);
    }

    const handleMoveSize = (e) => {
        setMoveSize(e.target.value);
    }

    const cautionTextAsHouseType = () => {
        if(currentHouseType === ""){
            return "집의 형태를 먼저 선택해주세요";
        } else if(currentHouseType === "monthlyRent"){
            return "단위 : 만원 & 월세 보증금을 입력해주세요";
        } else if(currentHouseType === "jeonse"){
            return "단위 : 만원 & 전세 보증금을 입력해주세요";
        } else if(currentHouseType === "purchaseSale"){
            return "단위 : 만원 & 현재 집 시세를 입력해주세요";
        }
    }
    
    const calculateTotalAmount = (a, b, c) => {
        setTotalAmount(a+b-c);
    }

    const handleButtonClick = () => {
        // 이름, 연봉, 저축한 금액, 현재 살고 있는 지역, 
        const data = {
            userName : userName,
            annualIncome : annualIncome,
            saveAmount : saveAmount,
            currentRegion : currentRegion,
            currentHouseType : currentHouseType,
            currentHousePrice : currentHousePrice,
            totalAmount : totalAmount,
            loanAmount : loanAmount,
            averageMonthlyExpenditure : averageMonthlyExpenditure,
            moveDate : moveDate,
            moveRegion : moveRegion,
            moveHouse : moveHouse,
            moveHouseType : moveHouseType,
            moveSize : moveSize
        };
        navigate('/result',{
            state:data
        })
    }

    return (
        <div>
            <AppHeader title={"KB-House User Information Input Page"}></AppHeader>
            <div id='user_input_background'>
                <h1 className='h1_title'>개인 정보 입력</h1>
                <table className='tType01'>
                    <colgroup>
                        <col width="23%"/>
                        <col/>
                    </colgroup>
                    <tbody>
                        <tr>
                            <th scope='row'>이름</th>
                            <td>
                                <input className='input' type='text' onChange={handleUserNameChange}></input>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>연봉</th>
                            <td>
                                <input className='input' type='number' onChange={handleAnnualIncomeChange}></input>
                                <span className='caution'>단위 : 만원 (ex. 7500만원인 경우 : 7500) & 세후 금액</span>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>저축한 금액</th>
                            <td>
                                <input className='input' type='number' onChange={handleSaveAmountChange}></input>
                                <span className='caution'>단위 : 만원 & 본인계좌에 있는 총 금액</span>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>현재 살고 있는 지역</th>
                            <td>
                                <div style={{display:'flex', flexDirection:'row'}}>
                                    <RegionCategory handleCurrentRegionChange={handleCurrentRegionChange}></RegionCategory>
                                    <span className='caution' style={{marginTop:"5px"}}>부모님 집에 거주하는 경우 대출 여부로 넘어가주세요</span>
                                </div>
                            </td>
                        </tr>
                        {(currentRegion !== "00" && currentRegion !== "") && (
                            <tr>
                                <th scope='row'>현재 살고 있는 집</th>
                                <td>
                                    <div style={{display:'flex', flexDirection:'row'}}>
                                        <select className='select' value={currentHouseType} style={{marginRight:"10px"}} onChange={handleCurrentHouseTypeChange}>
                                            <option value="">선택</option>
                                            <option value="monthlyRent">월세</option>
                                            <option value="jeonse">전세 </option>
                                            <option value="purchaseSale">매매</option>
                                        </select>
                                        <input className='input' type='number' onChange={handleCurrentHousePriceChange}></input>
                                        <span className='caution' style={{marginTop:"5px"}}>{cautionTextAsHouseType()}</span>
                                    </div>
                                </td>
                            </tr>
                        )}
                        <tr>
                            <th scope='row'>대출 여부</th>
                            <td>
                                <input className='input' type='number' onChange={handleLoanAmountChange}></input>
                                <span className='caution'>단위 : 만원 (ex. 대출 500만원 받은 경우 : 500) & 대출이 없으면 0 입력</span>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>순자산</th>
                            <td style={{height:"27px"}}>
                                {totalAmount}
                                <span className='caution'>단위 : 만원</span>    
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>평균 월 지출 비용</th>
                            <td>
                                <input className='input' type='number' onChange={handleAverageMonthlyExpenditureChange}></input>
                                <span className='caution'>단위 : 만원</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <h1 className='h1_title' style={{marginTop:"50px"}}>당신이 희망하는 집</h1>
                <table className='tType01'>
                    <colgroup>
                        <col width="23%"/>
                        <col/>
                    </colgroup>
                    <tbody>
                        <tr>
                            <th scope='row'>이사 가고 싶은 시기</th>
                            <td>
                                <input className='input' type='text' onChange={handleMoveDateChange} maxLength={2}></input>
                                <span className='caution'>개월 단위로 입력 (ex. 1년 6개월 뒤인 경우 : 18)</span>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>이사 가고 싶은 지역</th>
                            <td>
                                <RegionCategory handleCurrentRegionChange={handleMoveRegionChange}></RegionCategory>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>이사 가고 싶은 형태</th>
                            <td>
                                <div style={{display:'flex', flexDirection:'row'}}>
                                    <select className='select' value={moveHouse} onChange={handleMoveHouseChange} style={{marginRight:"10px"}}>
                                        <option value="">선택</option>
                                        <option value="apart">아파트</option>
                                        <option value="officetel">오피스텔</option>
                                    </select>
                                    <select className='select' value={moveHouseType} onChange={handleMoveHouseTypeChange}>
                                        <option value="">선택</option>
                                        <option value="jeonse">전세 </option>
                                        <option value="purchaseSale">매매</option>
                                    </select>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope='row'>이사 가고 싶은 평수</th>
                            <td>
                                <input className='input' type='number' onChange={handleMoveSize}></input>
                                <span className='caution'>평수로 입력</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div className='btnArea'>
                <button className='btnType01' onClick={handleButtonClick}>확인</button>
            </div>
        </div>
    );
};

export default UserInputPage;