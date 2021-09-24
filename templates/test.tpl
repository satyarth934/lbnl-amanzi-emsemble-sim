<amanzi_input type="unstructured" version="2.3.0">

    <materials>
      <material name="UUTRA">
        <comments>UUTRA</comments>
        <mechanical_properties>
          <porosity value="@Por@" />
          <particle_density value="2720.0" />
        </mechanical_properties>

        <permeability x="@Perm@" y="@Perm@" z="@Perm@" />
        <cap_pressure model="van_genuchten">
          <parameters alpha="@alpha@" m="@alpha@" optional_krel_smoothing_interval="500.0" sr="0.18" />
        </cap_pressure>
        <rel_perm model="mualem" />
        <assigned_regions>Upper_aquifer,Basin1,Basin2,Basin3,TopBarrier1,TopBarrier2,TopBarrier3,TopBarrier4,TopBarrier5</assigned_regions>
      </material>


      <material name="BARRIERS">
        <comments>BARRIES</comments>
        <mechanical_properties>
          <porosity value="@Por@" />
          <particle_density value="2720.0" />
        </mechanical_properties>

        <permeability x="@Perm@" y="@Perm@" z="@Perm@" />
        <cap_pressure model="van_genuchten">
          <parameters alpha="@alpha@" m="0.5" optional_krel_smoothing_interval="500.0" sr="0.18" />
        </cap_pressure>
        <rel_perm model="mualem" />
        <assigned_regions>Barrier1,Barrier2,Barrier3,Barrier4,Barrier5</assigned_regions>
      </material>

    </materials>

  </amanzi_input>
