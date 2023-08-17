import React from 'react';
import './newsElement.css'

const NewsElement = ({date, title, summary, url, img_url}) => {
  
    const openArticle = () => {
        window.open(url, '_blank');
    };
  
    return (
        <div className='news_element_background'>
            <div className='news_element_left' onClick={openArticle}>
                <img src={img_url} alt='news'/>
            </div>
            <div className='news_element_right'>
                <div className='news_element_title' onClick={openArticle}>
                    {title}
                </div>
                <div className='news_element_summary'>
                    {summary}
                </div>
                <div className='news_element_date'>
                    ⏱️ {date}
                </div>
            </div>
        </div>
    );
};

export default NewsElement;