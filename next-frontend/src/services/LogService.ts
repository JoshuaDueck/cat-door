export async function getRecentLogEntries() {
  return await fetch('http://localhost:5001/api/v1/log_entries', { next: { tags: ['log_entries'] }}).then(async (res) => {
    return await res.json()
  });
}
