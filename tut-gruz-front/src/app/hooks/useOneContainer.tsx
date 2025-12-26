import { useQuery } from "@tanstack/react-query";
import { containersService } from "../service/container.service";


export const useOneContainer = (container_id: string) => {
  const { data: container,
    error,
    isLoading,
  } = useQuery({ ...containersService.getOneContainerQueryOptions(container_id) })

  return { error, isLoading, container }
}