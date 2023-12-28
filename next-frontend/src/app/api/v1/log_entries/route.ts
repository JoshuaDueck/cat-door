export async function GET() {
  const res = await fetch('http://localhost:5001/api/v1/log_entries', {
    headers: {
      'Content-Type': 'application/json',
    },
    next: {
      tags: ['log_entries'],
    }
  })
  const data = await res.json()

  return Response.json({data})
}
