# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db = SQLAlchemy()

# # ------------------- USER MODEL ------------------- #
# class User(db.Model):
#     __tablename__ = 'user'  # explicit table name
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     role = db.Column(db.String(20), nullable=False)  # candidate or admin

#     # Relationship to resumes
#     resumes = db.relationship('Resume', backref='user', lazy=True)

#     def __repr__(self):
#         return f"<User {self.name} ({self.role})>"

# # ------------------- RESUME MODEL ------------------- #
# class Resume(db.Model):
#     __tablename__ = 'resume'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     file_name = db.Column(db.String(200), nullable=False)
#     parsed_text = db.Column(db.Text)
#     uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return f"<Resume {self.file_name} for User ID {self.user_id}>"


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ------------------- USER MODEL ------------------- #
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # candidate or admin

    resumes = db.relationship('Resume', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"


# ------------------- RESUME MODEL ------------------- #
class Resume(db.Model):
    __tablename__ = 'resume'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_name = db.Column(db.String(200), nullable=False)
    parsed_text = db.Column(db.Text)
    skills = db.Column(db.Text)  # ✅ Added field
    experience = db.Column(db.String(100))  # ✅ Added field
    suggested_roles = db.Column(db.String(255))  # ✅ Added field
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Resume {self.file_name} for User ID {self.user_id}>"
