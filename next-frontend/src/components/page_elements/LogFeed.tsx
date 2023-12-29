import { getRecentLogEntries } from "@/services/LogService"
import BasicFeed from "../lists/BasicFeed";

export default async function LogFeed({}:{}) {
  const log_entries = await getRecentLogEntries();

  const feed_data = log_entries['log_entries'].map((entry: any) => {
    let date = new Date(entry.timestamp * 1000)
    return {
      timestamp: date.toLocaleString('en-US', { timeZone: 'America/New_York' }),
      caption: entry.action,
    }
  })

  return (
    <div className="flex flex-row justify-between">
      <BasicFeed data={feed_data}/>
    </div>
  )
}
