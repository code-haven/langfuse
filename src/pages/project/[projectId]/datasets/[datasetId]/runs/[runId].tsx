import Header from "@/src/components/layouts/header";
import { DatasetRunItemsTable } from "@/src/features/datasets/components/DatasetRunItemsTable";
import { api } from "@/src/utils/api";
import { useRouter } from "next/router";

export default function Dataset() {
  const router = useRouter();
  const projectId = router.query.projectId as string;
  const datasetId = router.query.datasetId as string;
  const runId = router.query.runId as string;

  const dataset = api.datasets.byId.useQuery({
    datasetId,
    projectId,
  });

  return (
    <div>
      <Header
        title={`Dataset Run`}
        breadcrumb={[
          { name: "Datasets", href: `/project/${projectId}/datasets` },
          {
            name: dataset.data?.name ?? datasetId,
            href: `/project/${projectId}/datasets/${datasetId}`,
          },
          { name: "Run: " + runId },
        ]}
      />
      <DatasetRunItemsTable
        projectId={projectId}
        datasetId={datasetId}
        datasetRunId={runId}
      />
    </div>
  );
}
