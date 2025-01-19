import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VideoPlayer() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8080/api/videos')
      .then(response => {
        setVideos(response.data);
      })
      .catch(error => console.error('Error fetching videos:', error));
  }, []);

  return (
    <div>
      <h1>Video Streaming Platform</h1>
      <div>
        {videos.map((video) => (
          <div key={video.id}>
            <h2>{video.title}</h2>
            <video width="600" controls>
              <source src={`http://localhost:8080/api/video/${video.id}`} />
            </video>
          </div>
        ))}
      </div>
    </div>
  );
}

export default VideoPlayer;
