from db.db import SessionLocal
from db.models import Session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_session(session_id, data):
    db = SessionLocal()
    try:
        sess = db.query(Session).filter_by(session_id=session_id).first()
        if sess:
            sess.data = data
            logger.info(f"Sessão {session_id} atualizada")
        else:
            sess = Session(session_id=session_id, data=data)
            db.add(sess)
            logger.info(f"Nova sessão {session_id} criada")
        
        db.commit()
        return True
    except Exception as e:
        logger.error(f"Erro ao salvar sessão {session_id}: {e}")
        db.rollback()
        return False
    finally:
        db.close()

def load_session(session_id):
    db = SessionLocal()
    try:
        sess = db.query(Session).filter_by(session_id=session_id).order_by(Session.id.desc()).first()
        if sess:
            logger.info(f"Sessão {session_id} carregada com {len(sess.data)} mensagens")
            return sess.data
        else:
            logger.info(f"Sessão {session_id} não encontrada")
            return []
    except Exception as e:
        logger.error(f"Erro ao carregar sessão {session_id}: {e}")
        return []
    finally:
        db.close()