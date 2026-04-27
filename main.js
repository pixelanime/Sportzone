async function loadLiveScores() {
  try {
    const res = await fetch('scripts/scores.json');
    const data = await res.json();
    // contoh: tampilkan di #events (atau buat elemen baru)
    console.log('Live scores:', data);
    // TODO: render ke DOM sesuai kebutuhan
  } catch (e) {
    console.error('Failed to load scores', e);
  }
}
loadLiveScores();
