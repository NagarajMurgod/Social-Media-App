import "./post.css";
import MoreVertIcon from '@mui/icons-material/MoreVert';
import { Users } from "../../dummyData";
import { useState } from "react";
import { getImageUrl } from "../../utils";
import moment from 'moment';

export default function Post({ post }) {
  const [like,setLike] = useState(post.like)
  const [isLiked,setIsLiked] = useState(false)

  const likeHandler =()=>{
    setLike(isLiked ? like-1 : like+1)
    setIsLiked(!isLiked)
  }
  return (
    <div className="post">
      <div className="postWrapper">
        <div className="postTop">
          <div className="postTopLeft">
            <img
              className="postProfileImg"
              // src={getImageUrl(Users.filter((u) => u.id === post?.userId)[0].profilePicture)}
              src={post.profile_img}
              alt=""
            />
            <span className="postUsername">
              {/* {Users.filter((u) => u.id === post?.userId)[0].username} */}
              {post.username}
            </span>
            <span className="postDate">{moment(post.created_at).fromNow()}</span>
          </div>
          <div className="postTopRight">
            <MoreVertIcon />
          </div>
        </div>
        <div className="postCenter">
          <span className="postText">{post?.desc}</span>
          <img className="postImg" src={post.image} alt="" />
          {/* <img className="postImg" src={getImageUrl(post.photo)} alt="" /> */}
        </div>
        <div className="postBottom">
          <div className="postBottomLeft">
            <img className="likeIcon" src={getImageUrl("like.png")} onClick={likeHandler} alt="" />
            <img className="likeIcon" src={getImageUrl("heart.png")} onClick={likeHandler} alt="" />
            <span className="postLikeCounter">{post.like_count} people like it</span>
          </div>
          <div className="postBottomRight">
            <span className="postCommentText">{post.comments_count} comments</span>
          </div>
        </div>
      </div>
    </div>
  );
}
