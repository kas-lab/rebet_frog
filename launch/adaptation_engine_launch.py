from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from nav2_common.launch import ReplaceString


def generate_launch_description():

    config_files = os.path.join(get_package_share_directory("rebet_frog"), "config")
    schema_files = os.path.join(get_package_share_directory("typedb_tactics"), "schemas")

    engine_config_file = os.path.join(
        config_files,
        'adaptation_engine_config.yaml'
    )

    xtext_dir = os.path.join(get_package_share_directory("rebet_frog"), "xtext")

    engine_config_file = ReplaceString(
        source_file=engine_config_file,
        replacements={
            "<rebet_frog_xtext_dir>": (
                xtext_dir
            )
        },
    )


    typedb = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            os.path.join(get_package_share_directory("typedb_tactics"), "launch",
                         "tactical_retreat_kb.launch.py")
        ),
        launch_arguments={
            "schema_path": f"[{os.path.join(schema_files, 'data_structure', 'data_structure.tql')}, \
                              {os.path.join(schema_files, 'context_model', 'context_model.tql')}, \
                              {os.path.join(schema_files, 'ros_model', 'ros_model.tql')}, \
                              {os.path.join(schema_files, 'logical_expressions', 'logical_expression.tql')}, \
                              {os.path.join(schema_files, 'logical_expressions', 'fuzzy_expression.tql')}, \
                              {os.path.join(schema_files, 'feature_model', 'feature_model.tql')}, \
                              {os.path.join(schema_files, 'feature_model', 'feature_model_logical_expression.tql')}, \
                              {os.path.join(schema_files, 'tactics_model', 'tactics_model.tql')}, \
                              {os.path.join(schema_files, 'discover_tactics_model', 'discover_tactics_model.tql')}, \
                              {os.path.join(schema_files, 'relaxed', 'relaxed_model.tql')}]",
            # "data_path": f"[{os.path.join(config_files, 'insert_measurement.tql')}]",
            "force_database": "True",
            "force_data": "True",
        }.items(),
    )

    frog_adap_engine = Node(
        package="adapt_x",
        executable="adaptation_engine",
        output="screen",
        parameters=[engine_config_file]
    )

    return LaunchDescription(
        # [typedb]
        [typedb, frog_adap_engine]
        # [typedb, delay_adap_engine, aal, context_model]
        # [typedb, delay_adap_engine, aal, context_model] #, arborist, ]
    )
