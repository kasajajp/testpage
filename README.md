<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ジムコスト診断</title>

  <style>
    body {
      font-family: sans-serif;
      background: #0f0f0f;
      color: #fff;
      display: flex;
      justify-content: center;
      padding: 40px 16px;
    }

    .card {
      background: #1c1c1c;
      padding: 26px;
      border-radius: 18px;
      width: 100%;
      max-width: 420px;
    }

    h1 {
      text-align: center;
      font-size: 22px;
      margin-bottom: 18px;
    }

    input {
      width: 100%;
      padding: 14px;
      margin-top: 12px;
      border-radius: 10px;
      border: none;
      font-size: 16px;
    }

    button {
      width: 100%;
      margin-top: 14px;
      padding: 16px;
      border: none;
      border-radius: 12px;
      font-weight: bold;
      cursor: pointer;
      font-size: 16px;
    }

    .calc {
      background: #fff;
      color: #000;
    }

    .xpost {
      background: #000;
      color: #fff;
      border: 2px solid #444;
      font-size: 18px;
      padding: 18px;
    }

    .result {
      margin-top: 22px;
      font-size: 20px;
      font-weight: bold;
      text-align: center;
    }

    .comment {
      margin-top: 10px;
      text-align: center;
      color: #aaa;
      font-size: 14px;
    }

    .box {
      margin-top: 16px;
      padding: 14px;
      border: 1px solid #333;
      border-radius: 12px;
      text-align: center;
    }

    .box a {
      color: #fff;
      text-decoration: none;
      font-weight: bold;
    }

    .gymmap-title {
      margin-top: 18px;
      text-align: center;
      font-weight: bold;
      font-size: 14px;
      color: #aaa;
    }
  </style>
</head>

<body>

<div class="card">

  <h1>ジムコスト診断</h1>

  <input id="fee" type="number" placeholder="月額料金（例：8000）">
  <input id="visits" type="number" placeholder="月のジム回数（例：4）">

  <button class="calc" onclick="calc()">診断する</button>

  <div class="result" id="result"></div>
  <div class="comment" id="comment"></div>

  <button class="xpost" onclick="postToX()">Xでバズ投稿する 🚀</button>

  <div class="box" id="xbox"></div>

  <div class="gymmap-title">🏋️GymMap</div>

  <div class="box">
    <a href="https://kasajajp.github.io/kasaja_gymmap" target="_blank">
      あなたのジム料金は？
    </a>
  </div>

  <div style="margin-top: 16px; font-size: 12px; text-align:center; color:#666;">
    <a href="https://kasajajp.github.io/" style="color:#666;text-decoration:none;">
      KASAJA
    </a>
  </div>

</div>

<script>
let lastText = "";

function calc() {
  const fee = Number(document.getElementById("fee").value);
  const visits = Number(document.getElementById("visits").value);

  if (!fee || !visits) return;

  const per = fee / visits;

  let label = "";

  if (per >= 10000) label = "富豪パーソナル級";
  else if (per >= 8000) label = "パーソナル級";
  else if (per >= 4000) label = "高級会員級";
  else if (per >= 2000) label = "ダンベル級";
  else if (per >= 1000) label = "公園トレ級";
  else if (per >= 500) label = "牛丼級";
  else label = "異常コスパ級";

  lastText = `ジム1回 ${Math.round(per)}円 → ${label}`;

  document.getElementById("result").innerText = lastText;
  document.getElementById("comment").innerText = "X投稿で共有可能";
}

function postToX() {
  if (!lastText) {
    alert("先に診断してください");
    return;
  }

  const hashtags = [
    "#ジムコスト診断",
    "#筋トレ",
    "#フィットネス",
    "#ジム通い"
  ].join(" ");

  const text =
`【ジムコスト診断｜KASAJA】
${lastText}

${hashtags}

診断はこちら👇
https://kasajajp.github.io/tobacco_healthcare_hp/`;

  const url =
    `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`;

  window.open(url, "_blank");

  document.getElementById("xbox").innerText =
    "X投稿画面を開きました";
}
</script>

</body>
</html>
