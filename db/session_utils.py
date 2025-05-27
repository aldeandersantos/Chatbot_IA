from db.db import SessionLocal
from db.models import Session
from sqlalchemy import func

def get_session_stats():
    db = SessionLocal()
    try:
        total_sessions = db.query(Session).count()
        oldest_session = db.query(Session).order_by(Session.created_at.asc()).first()
        newest_session = db.query(Session).order_by(Session.created_at.desc()).first()
        
        stats = {
            'total_sessions': total_sessions,
            'oldest_session_date': oldest_session.created_at if oldest_session else None,
            'newest_session_date': newest_session.created_at if newest_session else None
        }
        return stats
    finally:
        db.close()

def list_all_sessions():
    db = SessionLocal()
    try:
        sessions = db.query(Session).order_by(Session.created_at.desc()).all()
        session_list = []
        for sess in sessions:
            messages_count = len(sess.data) if sess.data else 0
            session_list.append({
                'session_id': sess.session_id,
                'created_at': sess.created_at,
                'messages_count': messages_count
            })
        return session_list
    finally:
        db.close()

def delete_session(session_id):
    db = SessionLocal()
    try:
        sess = db.query(Session).filter_by(session_id=session_id).first()
        if sess:
            db.delete(sess)
            db.commit()
            return True
        return False
    finally:
        db.close()

def cleanup_old_sessions(days_old=30):
    from datetime import datetime, timedelta
    
    db = SessionLocal()
    try:
        cutoff_date = datetime.now() - timedelta(days=days_old)
        old_sessions = db.query(Session).filter(Session.created_at < cutoff_date).all()
        
        count = len(old_sessions)
        for sess in old_sessions:
            db.delete(sess)
        
        db.commit()
        return count
    finally:
        db.close()
