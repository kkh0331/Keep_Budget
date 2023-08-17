import React, { useEffect, useState } from 'react';
import '../components/main/mainNews.css'
import MoveRegionChange from '../components/common/MoveRegionChange';
import WordCloudChart from '../components/main/WordCloudChart';
import axios from 'axios';
import NewsElement from '../components/main/NewsElement';

const MainMiddlePage = (props) => {

    const {getMoveRegion} = MoveRegionChange();
    const moveRegion = getMoveRegion(props.wantMoveRegion);
    const [wordCloudData, setWordCloudData] = useState([]);
    const [accidentNewsData, setAccidentNewsData] = useState([]);

    useEffect(() => {
        getAccidentNews();
    },[moveRegion])

    const getAccidentNews = () => {
        let option = {
            url: "/accident_news",
            method: "POST",
            data:{
                move_region: moveRegion
            }
        }
        axios(option).then(({data}) => {
            setWordCloudData(data.wordCloudData);
            setAccidentNewsData(data.accidentNewsData);
        }).catch((error) => {
            console.log(error);
        })
    }

    return (
        <div>
            <h2 className='h2_title'>{moveRegion} 사건사고 뉴스 Word Cloud</h2>
            <WordCloudChart wordCloudData={wordCloudData}></WordCloudChart>
            <div className='div_news_element'>
                {accidentNewsData.map((news) => {
                    return <NewsElement date={news.date} title={news.title} summary={news.summary} url={news.url} img_url={news.img_url}></NewsElement>
                })}
            </div>
        </div>
    );
};

export default MainMiddlePage;