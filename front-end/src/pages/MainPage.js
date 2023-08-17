import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import AppHeader from '../components/common/AppHeader';
import '../components/main/main.css';
import RightTop from '../components/main/RightTop';
import MainLeftPage from './MainLeftPage';
import MainMiddlePage from './MainMiddlePage';
import SearchMove from '../components/main/SearchMove';

const MainPage = () => {

    const location = useLocation();
    const userInfo = {...location.state}
    const [wantMoveRegion, setWantMoveRegion] = useState(userInfo.moveRegion)

    return (
        <div>
            <AppHeader title={"KB-House Main Page"}></AppHeader>
            <div className='app-container'>
                <div className='left-section'>
                    <MainLeftPage wantMoveRegion={wantMoveRegion}></MainLeftPage>
                </div>
                <div className='left-section'>
                    <MainMiddlePage wantMoveRegion={wantMoveRegion}></MainMiddlePage>
                </div>
                <div className='right-section'>
                    <div className='top-right-section'>
                        <RightTop userInfo={userInfo} wantMoveRegion={wantMoveRegion}></RightTop>
                    </div>
                    <div className='middle-right-section'>
                        <SearchMove setWantMoveRegion={setWantMoveRegion}></SearchMove>
                    </div>
                    <div className='bottom-right-section'>
                        chatgpt
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MainPage;