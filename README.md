<script>
fetch("data.json")
  .then(res => res.json())
  .then(data => {
    document.body.innerHTML = data.map(d => `
      <div style="border:1px solid #333; margin:10px; padding:10px;">
        <div>${d.slug}</div>
        <div>${d.price ?? "不明"}</div>
        <div>${d.address ?? "不明"}</div>
        <a href="${d.url}" target="_blank">開く</a>
      </div>
    `).join("");
  });
</script>
