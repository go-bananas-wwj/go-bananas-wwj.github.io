const notes = import.meta.glob('./notes/*.md', { as: 'raw', eager: true });

export function getAllNotes() {
  const list = [];
  for (const path in notes) {
    const raw = notes[path];
    const slug = path.replace(/^.*\//, '').replace(/\.md$/, '');
    const frontmatter = parseFrontmatter(raw);
    list.push({
      slug,
      title: frontmatter.title || slug,
      date: frontmatter.date || '',
      tags: frontmatter.tags ? frontmatter.tags.split(',').map(t => t.trim()) : [],
      summary: frontmatter.summary || extractSummary(raw),
      raw,
    });
  }
  return list.sort((a, b) => new Date(b.date) - new Date(a.date));
}

export function getNoteBySlug(slug) {
  const all = getAllNotes();
  return all.find(n => n.slug === slug);
}

function parseFrontmatter(raw) {
  const match = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n/);
  if (!match) return {};
  const fm = {};
  match[1].split('\n').forEach(line => {
    const idx = line.indexOf(':');
    if (idx > 0) {
      const key = line.slice(0, idx).trim();
      const val = line.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
      fm[key] = val;
    }
  });
  return fm;
}

function extractSummary(raw) {
  const body = raw.replace(/^---\s*\n[\s\S]*?\n---\s*\n/, '');
  return body.replace(/[#*_`>\-\[\]\(\)!]/g, '').slice(0, 120) + '...';
}
