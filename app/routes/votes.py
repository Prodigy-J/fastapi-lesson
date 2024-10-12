from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from .auth import oauth2

router = APIRouter(prefix="/vote", tags=["vote"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"You have already liked post {vote.post_id}")
        try:
            new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
            db.add(new_vote)
            db.commit()
            db.refresh(new_vote)
            return {"message": f"You have successfully liked post {vote.post_id}"}
        except Exception:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The post does not exist")
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"You have not liked post {vote.post_id}")
        old_vote = vote_query.first()
        db.delete(old_vote)
        db.commit()
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Your like has been removed from post {vote.post_id}")
