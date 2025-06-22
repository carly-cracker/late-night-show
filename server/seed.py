from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User
from datetime import datetime

app = create_app()

with app.app_context():
    print("Seeding database...")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    g1 = Guest(name="Beyoncé", occupation="Musician")
    g2 = Guest(name="Chris Evans", occupation="Actor")

    e1 = Episode(date=datetime(2024, 6, 1), number=1)
    e2 = Episode(date=datetime(2024, 6, 2), number=2)

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)


    u1 = User(username="admin")
    u1.password_hash = "password123"  

    db.session.add_all([g1, g2, e1, e2, a1, a2, u1])
    db.session.commit()

    print("Done seeding!")
