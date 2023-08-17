import React, { useEffect, useState } from 'react';
import MoveRegionChange from '../components/common/MoveRegionChange';
import '../components/main/mainNews.css'
import NewsDonutChart from '../components/main/NewsDonutChart';
import axios from 'axios';
import NewsElement from '../components/main/NewsElement';

const MainLeftPage = (props) => {

    const {getMoveRegion} = MoveRegionChange();
    const moveRegion = getMoveRegion(props.wantMoveRegion);
    const [selectedItem, setSelectedItem] = useState("중립");

    const [newsList, setNewsList] = useState([]);

    const handleStateClick = (item) => {
        setSelectedItem(item.label);
    }

    const getNewsList = () => {
        let option = {
            url: "/real_state_news_element",
            method: "POST",
            data:{
                move_region: moveRegion,
                selected_item: selectedItem
            }
        }
        axios(option).then(({data}) => {
            console.log(data);
            setNewsList(data);
        }).catch((error) => {
            console.log(error);
        })
    }

    useEffect(() => {
        getNewsList();
    },[selectedItem])

    useEffect(() => {
        getNewsList();
    },[moveRegion])

    return (
        <div>
            <h2 className='h2_title'>{moveRegion} 부동산 뉴스 감정 분석</h2>
            <NewsDonutChart moveRegion={moveRegion} handleStateClick={handleStateClick}></NewsDonutChart>
            <div className='div_news_element'>
                {newsList.map((news) => {
                    return <NewsElement date={news.date} title={news.title} summary={news.summary} url={news.url} img_url={news.img_url}></NewsElement>
                })}
            </div>
        </div>
    );
};

export default MainLeftPage;