"use server";

import { revalidateTag } from "next/cache";

export default async function revalidateDoor() {
  revalidateTag("door");
}
