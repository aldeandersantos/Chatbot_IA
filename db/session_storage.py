from db.db import SessionLocal
from db.models import Session

def save_session(session_id, data):
    db = SessionLocal()
    sess = db.query(Session).filter_by(session_id=session_id).first()
    if sess:
        sess.data = data
    else:
        sess = Session(session_id=session_id, data=data)
        db.add(sess)
    db.commit()
    db.close()

def load_session(session_id):
    db = SessionLocal()
    sess = db.query(Session).filter_by(session_id=session_id).order_by(Session.id.desc()).first()
    db.close()
    if sess:
        return sess.data
    return []