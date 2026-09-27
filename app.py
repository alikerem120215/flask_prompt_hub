import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev_secret_key_for_prompt_hub'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prompts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tag = db.Column(db.String(50), nullable=True, default='General')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Prompt {self.title}>'

@app.route('/')
def index():
    tag_filter = request.args.get('tag')
    if tag_filter:
        prompts = Prompt.query.filter_by(tag=tag_filter).order_by(Prompt.created_at.desc()).all()
    else:
        prompts = Prompt.query.order_by(Prompt.created_at.desc()).all()
        
    tags = db.session.query(Prompt.tag).distinct().all()
    tags = [t[0] for t in tags if t[0]]
    
    return render_template('index.html', prompts=prompts, tags=tags, current_tag=tag_filter)

@app.route('/add', methods=['POST'])
def add_prompt():
    title = request.form.get('title')
    content = request.form.get('content')
    tag = request.form.get('tag') or 'General'

    if title and content:
        new_prompt = Prompt(title=title, content=content, tag=tag)
        db.session.add(new_prompt)
        db.session.commit()
        flash('Prompt başarıyla eklendi!', 'success')
    else:
        flash('Lütfen başlık ve içerik alanlarını doldurun.', 'error')

    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_prompt(id):
    prompt = Prompt.query.get_or_404(id)
    db.session.delete(prompt)
    db.session.commit()
    flash('Prompt silindi.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
