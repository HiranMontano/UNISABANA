import streamlit as st

st.set_page_config(
    page_title="Universidad de La Sabana",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS global ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

:root {
    --blue:   #003087;
    --teal:   #00A9A5;
    --lgray:  #f5f6f8;
    --dgray:  #444;
    --white:  #ffffff;
}

html, body, [class*="css"] {
    font-family: 'Open Sans', sans-serif;
    margin: 0; padding: 0;
}

/* hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── TOP BAR ── */
.topbar {
    background: var(--blue);
    color: #cdd8e8;
    font-size: 12px;
    padding: 6px 40px;
    display: flex;
    justify-content: flex-end;
    gap: 20px;
}
.topbar a { color: #cdd8e8; text-decoration: none; }
.topbar a:hover { color: #fff; }

/* ── HEADER ── */
.header {
    background: var(--white);
    border-bottom: 3px solid var(--teal);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 40px;
}
.logo-text {
    font-size: 26px;
    font-weight: 700;
    color: var(--blue);
    letter-spacing: -0.5px;
    line-height: 1.1;
}
.logo-text span { color: var(--teal); }
.header-right {
    display: flex;
    align-items: center;
    gap: 16px;
}
.btn-contact {
    background: var(--teal);
    color: #fff !important;
    border: none;
    border-radius: 4px;
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
}
.btn-contact:hover { background: #008a87; }

/* ── NAV ── */
.navbar {
    background: var(--blue);
    display: flex;
    gap: 0;
    padding: 0 40px;
    overflow-x: auto;
}
.navbar a {
    color: #c8d8ee;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
    padding: 14px 16px;
    white-space: nowrap;
    border-bottom: 3px solid transparent;
    transition: .2s;
}
.navbar a:hover, .navbar a.active {
    color: #fff;
    border-bottom: 3px solid var(--teal);
}

/* ── HERO ── */
.hero {
    background: linear-gradient(135deg, var(--blue) 0%, #005b9f 60%, #00A9A5 100%);
    color: #fff;
    padding: 80px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.hero h1 {
    font-size: 46px;
    font-weight: 700;
    margin: 0 0 10px;
    position: relative;
}
.hero h1 span { color: #7ee8e6; }
.hero p {
    font-size: 20px;
    opacity: .9;
    max-width: 680px;
    margin: 0 auto 30px;
    position: relative;
}
.hero-btns { display: flex; gap: 16px; justify-content: center; position: relative; }
.btn-primary {
    background: var(--teal);
    color: #fff;
    border: none;
    border-radius: 4px;
    padding: 13px 30px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
}
.btn-outline {
    background: transparent;
    color: #fff;
    border: 2px solid #fff;
    border-radius: 4px;
    padding: 11px 28px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
}
.btn-outline:hover { background: rgba(255,255,255,.15); }

/* ── STATS STRIP ── */
.stats-strip {
    background: var(--teal);
    display: flex;
    justify-content: space-around;
    padding: 28px 40px;
    color: #fff;
    text-align: center;
}
.stat-item h3 { font-size: 34px; font-weight: 700; margin: 0; }
.stat-item p  { font-size: 13px; margin: 4px 0 0; opacity: .9; }

/* ── SECTION TITLE ── */
.section-wrap { padding: 60px 40px; }
.section-wrap.gray { background: var(--lgray); }
.section-title {
    text-align: center;
    margin-bottom: 40px;
}
.section-title h2 {
    font-size: 30px;
    font-weight: 700;
    color: var(--blue);
    margin: 0 0 8px;
}
.section-title p { color: var(--dgray); font-size: 15px; margin: 0; }
.section-title .line {
    width: 60px; height: 4px;
    background: var(--teal);
    margin: 12px auto 0;
    border-radius: 2px;
}

/* ── CARDS ── */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 24px;
}
.card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 3px 14px rgba(0,0,0,.09);
    overflow: hidden;
    transition: transform .2s, box-shadow .2s;
}
.card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,.13); }
.card-img {
    height: 160px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 52px;
}
.card-body { padding: 20px; }
.card-body h4 { font-size: 16px; font-weight: 700; color: var(--blue); margin: 0 0 8px; }
.card-body p  { font-size: 13px; color: var(--dgray); margin: 0 0 14px; line-height: 1.5; }
.card-tag {
    display: inline-block;
    background: #e8f4ff;
    color: var(--blue);
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 10px;
}
.card-link {
    color: var(--teal);
    font-size: 13px;
    font-weight: 700;
    text-decoration: none;
}

/* ── SEARCH BOX ── */
.search-box {
    background: var(--white);
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,.10);
    padding: 32px 36px;
    max-width: 860px;
    margin: 0 auto 48px;
}
.search-box h3 {
    font-size: 20px;
    font-weight: 700;
    color: var(--blue);
    margin: 0 0 20px;
    text-align: center;
}
.filter-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr auto;
    gap: 12px;
    align-items: end;
}
.filter-row label { font-size: 12px; font-weight: 600; color: var(--dgray); display: block; margin-bottom: 4px; }
.filter-row select {
    width: 100%;
    padding: 10px 12px;
    border: 1.5px solid #d0d8e4;
    border-radius: 6px;
    font-size: 13px;
    color: var(--dgray);
    background: #fff;
}
.btn-search {
    background: var(--blue);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 11px 22px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    white-space: nowrap;
}

/* ── TESTIMONIALS ── */
.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
}
.testimonial-card {
    background: #fff;
    border-radius: 10px;
    padding: 28px 24px;
    box-shadow: 0 3px 14px rgba(0,0,0,.08);
    border-left: 4px solid var(--teal);
}
.testimonial-card p {
    font-size: 14px;
    color: #555;
    font-style: italic;
    margin: 0 0 18px;
    line-height: 1.6;
}
.testimonial-author { display: flex; align-items: center; gap: 12px; }
.avatar {
    width: 44px; height: 44px;
    border-radius: 50%;
    background: var(--blue);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 700;
    flex-shrink: 0;
}
.author-info strong { display: block; font-size: 13px; color: var(--blue); font-weight: 700; }
.author-info span   { font-size: 12px; color: #888; }

/* ── NEWS ── */
.news-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 24px;
}
.news-card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 3px 14px rgba(0,0,0,.08);
    overflow: hidden;
}
.news-img {
    height: 140px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    background: var(--lgray);
}
.news-body { padding: 18px 20px; }
.news-date { font-size: 11px; color: #999; margin: 0 0 6px; font-weight: 600; }
.news-body h4 { font-size: 15px; font-weight: 700; color: var(--blue); margin: 0 0 8px; line-height: 1.4; }
.news-body p  { font-size: 13px; color: #666; margin: 0; line-height: 1.5; }

/* ── EVENTS ── */
.events-list { display: flex; flex-direction: column; gap: 16px; max-width: 760px; margin: 0 auto; }
.event-item {
    display: flex;
    gap: 20px;
    background: #fff;
    border-radius: 10px;
    padding: 20px 24px;
    box-shadow: 0 3px 14px rgba(0,0,0,.08);
    align-items: center;
}
.event-date {
    background: var(--blue);
    color: #fff;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    min-width: 60px;
    flex-shrink: 0;
}
.event-date .day   { font-size: 24px; font-weight: 700; line-height: 1; }
.event-date .month { font-size: 11px; font-weight: 600; opacity: .8; margin-top: 2px; }
.event-info h4 { font-size: 15px; font-weight: 700; color: var(--blue); margin: 0 0 4px; }
.event-info p  { font-size: 13px; color: #666; margin: 0; }
.event-tag {
    margin-left: auto;
    background: #e8f4ff;
    color: var(--blue);
    font-size: 11px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    white-space: nowrap;
}

/* ── CONTACT STRIP ── */
.contact-strip {
    background: linear-gradient(90deg, var(--blue) 0%, #005b9f 100%);
    color: #fff;
    text-align: center;
    padding: 56px 40px;
}
.contact-strip h2 { font-size: 28px; font-weight: 700; margin: 0 0 10px; }
.contact-strip p  { font-size: 16px; opacity: .85; margin: 0 0 28px; }

/* ── FOOTER ── */
.footer {
    background: #0a1628;
    color: #b0bdd0;
    padding: 50px 40px 20px;
}
.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 40px;
    margin-bottom: 36px;
}
.footer-brand .logo-text { font-size: 20px; }
.footer-brand p { font-size: 13px; margin: 12px 0 20px; line-height: 1.6; color: #8a9bb5; }
.social-icons { display: flex; gap: 10px; flex-wrap: wrap; }
.social-icon {
    width: 34px; height: 34px;
    border-radius: 50%;
    background: #1e2d45;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    cursor: pointer;
    transition: background .2s;
    text-decoration: none;
}
.social-icon:hover { background: var(--teal); }
.footer-col h5 {
    font-size: 13px;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: .6px;
    margin: 0 0 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #1e2d45;
}
.footer-col a {
    display: block;
    color: #8a9bb5;
    text-decoration: none;
    font-size: 13px;
    margin-bottom: 8px;
    transition: color .2s;
}
.footer-col a:hover { color: var(--teal); }
.footer-bottom {
    border-top: 1px solid #1e2d45;
    padding-top: 20px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
    font-size: 12px;
    color: #566880;
}
</style>
""", unsafe_allow_html=True)


# ── TOP BAR ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <a href="#">Aspirantes</a>
    <a href="#">Estudiantes</a>
    <a href="#">Egresados</a>
    <a href="#">Docentes</a>
    <a href="#">Empleadores</a>
    <span>🇨🇴 ES &nbsp;|&nbsp; 🇺🇸 EN</span>
</div>
""", unsafe_allow_html=True)

# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header">
    <div class="logo-text">Uni<span>Sabana</span><br>
        <span style="font-size:11px;font-weight:400;color:#666;letter-spacing:0">Universidad de La Sabana</span>
    </div>
    <div class="header-right">
        <input type="text" placeholder="🔍  Buscar..." style="
            padding:8px 14px;border:1.5px solid #d0d8e4;
            border-radius:4px;font-size:13px;width:220px;">
        <a class="btn-contact" href="#">📞 Contáctanos</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NAVBAR ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    <a href="#" class="active">La Universidad</a>
    <a href="#">Programas</a>
    <a href="#">Admisiones y Becas</a>
    <a href="#">Investigación</a>
    <a href="#">Bienestar</a>
    <a href="#">Biblioteca</a>
    <a href="#">Impacto Tangible</a>
    <a href="#">Noticias y Prensa</a>
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Bienvenido a la <span>UniSabana Xperience</span></h1>
    <p>Un modelo académico humanista, experiencial e innovador que transforma personas y construye un mundo mejor.</p>
    <div class="hero-btns">
        <a class="btn-primary" href="#">Explora nuestros programas</a>
        <a class="btn-outline" href="#">Admisiones 2026–2027</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── STATS STRIP ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-strip">
    <div class="stat-item"><h3>187</h3><p>Programas académicos</p></div>
    <div class="stat-item"><h3>+30.000</h3><p>Estudiantes activos</p></div>
    <div class="stat-item"><h3>Top 3</h3><p>Universidades privadas en Colombia</p></div>
    <div class="stat-item"><h3>+70</h3><p>Países con convenios internacionales</p></div>
    <div class="stat-item"><h3>60 años</h3><p>De excelencia académica</p></div>
</div>
""", unsafe_allow_html=True)

# ── PROGRAM FINDER ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section-wrap">
    <div class="section-title">
        <h2>Encuentra tu programa</h2>
        <p>Más de 187 programas formales para impulsar tu futuro</p>
        <div class="line"></div>
    </div>
    <div class="search-box">
        <h3>🔍 Buscar programas académicos</h3>
        <div class="filter-row">
            <div>
                <label>Nivel académico</label>
                <select>
                    <option>Todos los niveles</option>
                    <option>Pregrado</option>
                    <option>Posgrado</option>
                    <option>Educación continua</option>
                </select>
            </div>
            <div>
                <label>Unidad académica</label>
                <select>
                    <option>Todas las unidades</option>
                    <option>Escuela Internacional de Ciencias Económicas</option>
                    <option>Facultad de Derecho y Ciencias Políticas</option>
                    <option>Facultad de Ingeniería</option>
                    <option>Facultad de Medicina</option>
                    <option>Facultad de Psicología</option>
                </select>
            </div>
            <div>
                <label>Modalidad</label>
                <select>
                    <option>Todas las modalidades</option>
                    <option>Presencial</option>
                    <option>Híbrido</option>
                    <option>Virtual</option>
                </select>
            </div>
            <div>
                <button class="btn-search">Buscar →</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Program cards
st.markdown("""
    <div class="cards-grid">
        <div class="card">
            <div class="card-img" style="background:#e8f4ff;">📊</div>
            <div class="card-body">
                <span class="card-tag">Pregrado</span>
                <h4>Administración de Empresas</h4>
                <p>Forma líderes con visión global, ética y capacidad de gestión en entornos cambiantes.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
        <div class="card">
            <div class="card-img" style="background:#e8fff4;">⚕️</div>
            <div class="card-body">
                <span class="card-tag">Pregrado</span>
                <h4>Medicina</h4>
                <p>Programa acreditado de alta calidad con énfasis en humanismo y práctica clínica integral.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
        <div class="card">
            <div class="card-img" style="background:#fff8e8;">⚖️</div>
            <div class="card-body">
                <span class="card-tag">Pregrado</span>
                <h4>Derecho</h4>
                <p>Formación jurídica con sólidos fundamentos éticos, filosóficos y práctica profesional.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
        <div class="card">
            <div class="card-img" style="background:#f0e8ff;">🔐</div>
            <div class="card-body">
                <span class="card-tag">Posgrado</span>
                <h4>Diplomado en Ciberseguridad</h4>
                <p>Especialización práctica en protección de sistemas, redes y datos empresariales.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
        <div class="card">
            <div class="card-img" style="background:#ffe8ee;">🧠</div>
            <div class="card-body">
                <span class="card-tag">Maestría</span>
                <h4>Psicología Educativa</h4>
                <p>Profundiza en procesos de aprendizaje, desarrollo humano e intervención en contextos educativos.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
        <div class="card">
            <div class="card-img" style="background:#e8f8ff;">🌐</div>
            <div class="card-body">
                <span class="card-tag">Pregrado</span>
                <h4>Relaciones Internacionales</h4>
                <p>Prepara profesionales con visión global para los retos diplomáticos y geopolíticos actuales.</p>
                <a class="card-link" href="#">Ver programa →</a>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TESTIMONIALS ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-wrap gray">
    <div class="section-title">
        <h2>Lo que dicen nuestros egresados</h2>
        <p>Profesionales de impacto en las mejores empresas del mundo</p>
        <div class="line"></div>
    </div>
    <div class="testimonial-grid">
        <div class="testimonial-card">
            <p>"La Sabana me dio las herramientas para pensar de manera crítica y ética. Hoy lidero proyectos de impacto global en Chevron."</p>
            <div class="testimonial-author">
                <div class="avatar">M</div>
                <div class="author-info">
                    <strong>María Fernanda Ríos</strong>
                    <span>Ingeniería Industrial · Chevron</span>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p>"Mi formación humanista en La Sabana fue clave para entender al usuario en Google. La tecnología con propósito es posible."</p>
            <div class="testimonial-author">
                <div class="avatar">C</div>
                <div class="author-info">
                    <strong>Carlos Mendoza</strong>
                    <span>Comunicación · Google</span>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p>"La calidad académica y la red de egresados me abrieron puertas que nunca imaginé. Hoy hago ciencia de datos en J&J."</p>
            <div class="testimonial-author">
                <div class="avatar">A</div>
                <div class="author-info">
                    <strong>Ana Lucía Torres</strong>
                    <span>Medicina · Johnson & Johnson</span>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p>"El ambiente universitario, los profesores y los valores que viví en La Sabana son la base de mi carrera política."</p>
            <div class="testimonial-author">
                <div class="avatar">J</div>
                <div class="author-info">
                    <strong>Jorge Patiño</strong>
                    <span>Ciencias Políticas · Congreso de Colombia</span>
                </div>
            </div>
        </div>
        <div class="testimonial-card">
            <p>"Emprender fue mi sueño y La Sabana me dio el ecosistema perfecto: mentoría, red de contactos y una formación integral."</p>
            <div class="testimonial-author">
                <div class="avatar">V</div>
                <div class="author-info">
                    <strong>Valentina Cruz</strong>
                    <span>Administración · CEO Startup Fintech</span>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── NEWS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-wrap">
    <div class="section-title">
        <h2>Noticias y Prensa</h2>
        <p>Logros, investigaciones y vida universitaria</p>
        <div class="line"></div>
    </div>
    <div class="news-grid">
        <div class="news-card">
            <div class="news-img">🏆</div>
            <div class="news-body">
                <p class="news-date">14 MAYO 2026</p>
                <h4>Investigadora de La Sabana gana premio internacional de ciencias de la salud</h4>
                <p>La doctora Patricia Gómez fue reconocida por su trabajo en oncología molecular en el congreso de Harvard.</p>
            </div>
        </div>
        <div class="news-card">
            <div class="news-img">🚀</div>
            <div class="news-body">
                <p class="news-date">08 MAYO 2026</p>
                <h4>Startup de estudiantes de Ingeniería recibe inversión de $500.000 USD</h4>
                <p>El proyecto AgriTech de tres estudiantes de quinto semestre obtuvo financiación de un fondo de Silicon Valley.</p>
            </div>
        </div>
        <div class="news-card">
            <div class="news-img">📚</div>
            <div class="news-body">
                <p class="news-date">02 MAYO 2026</p>
                <h4>La Sabana escala al top 5 de universidades más innovadoras de Colombia</h4>
                <p>El ranking Sapiens Research 2026 reconoce la producción científica y el impacto social de la institución.</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── EVENTS ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-wrap gray">
    <div class="section-title">
        <h2>Próximos Eventos</h2>
        <p>Conferencias, Open Campus y actividades de bienestar</p>
        <div class="line"></div>
    </div>
    <div class="events-list">
        <div class="event-item">
            <div class="event-date"><div class="day">22</div><div class="month">MAY</div></div>
            <div class="event-info">
                <h4>Open Campus – Conoce La Sabana</h4>
                <p>📍 Campus Universitario, Chía &nbsp;·&nbsp; 🕙 9:00 a.m. – 1:00 p.m.</p>
            </div>
            <span class="event-tag">Aspirantes</span>
        </div>
        <div class="event-item">
            <div class="event-date"><div class="day">28</div><div class="month">MAY</div></div>
            <div class="event-info">
                <h4>Simposio Internacional de Inteligencia Artificial y Derecho</h4>
                <p>📍 Auditorio Central &nbsp;·&nbsp; 🕙 8:00 a.m. – 5:00 p.m.</p>
            </div>
            <span class="event-tag">Académico</span>
        </div>
        <div class="event-item">
            <div class="event-date"><div class="day">05</div><div class="month">JUN</div></div>
            <div class="event-info">
                <h4>Feria de Bienestar y Salud Mental Universitaria</h4>
                <p>📍 Plazoleta Central &nbsp;·&nbsp; 🕙 10:00 a.m. – 3:00 p.m.</p>
            </div>
            <span class="event-tag">Bienestar</span>
        </div>
        <div class="event-item">
            <div class="event-date"><div class="day">12</div><div class="month">JUN</div></div>
            <div class="event-info">
                <h4>Webinar: Cómo financiar tu posgrado en La Sabana</h4>
                <p>💻 Virtual (Zoom) &nbsp;·&nbsp; 🕙 6:00 p.m. – 7:30 p.m.</p>
            </div>
            <span class="event-tag">Virtual</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT CTA ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-strip">
    <h2>¿Listo para comenzar tu historia en La Sabana?</h2>
    <p>Nuestro equipo de admisiones está disponible para orientarte en cada paso del proceso.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
        <a class="btn-primary" href="#">📞 Llámanos ahora</a>
        <a class="btn-outline" href="#">💬 WhatsApp</a>
        <a class="btn-outline" href="#">✉️ Escríbenos</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div class="footer-brand">
            <div class="logo-text">Uni<span>Sabana</span></div>
            <p>Universidad de La Sabana · Campus del Puente del Común, Km 7, Autopista Norte de Bogotá, Chía, Cundinamarca.</p>
            <div class="social-icons">
                <a class="social-icon" href="#">🐦</a>
                <a class="social-icon" href="#">📘</a>
                <a class="social-icon" href="#">📸</a>
                <a class="social-icon" href="#">💼</a>
                <a class="social-icon" href="#">🎵</a>
                <a class="social-icon" href="#">▶️</a>
            </div>
        </div>
        <div class="footer-col">
            <h5>Navegación</h5>
            <a href="#">La Universidad</a>
            <a href="#">Programas académicos</a>
            <a href="#">Admisiones</a>
            <a href="#">Investigación</a>
            <a href="#">Bienestar</a>
            <a href="#">Biblioteca</a>
        </div>
        <div class="footer-col">
            <h5>Comunidad</h5>
            <a href="#">Portal estudiantes</a>
            <a href="#">Portal docentes</a>
            <a href="#">Red de egresados</a>
            <a href="#">Calendario académico</a>
            <a href="#">Donaciones</a>
            <a href="#">Trabaja con nosotros</a>
        </div>
        <div class="footer-col">
            <h5>Contacto</h5>
            <a href="#">📞 (601) 861 5555</a>
            <a href="#">💬 WhatsApp</a>
            <a href="#">✉️ info@unisabana.edu.co</a>
            <a href="#">🗺️ Cómo llegar</a>
            <a href="#">Política de datos</a>
            <a href="#">Política de cookies</a>
        </div>
    </div>
    <div class="footer-bottom">
        <span>© 2026 Universidad de La Sabana · SNIES 1711 · Institución de Educación Superior sujeta a inspección y vigilancia del MEN.</span>
        <span>Resolución MEN 2513 de 1971 · Personería Jurídica 1112 del 7 de julio de 1979</span>
    </div>
</div>
""", unsafe_allow_html=True)
